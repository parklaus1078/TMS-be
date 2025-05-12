from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.ai_solutions.ai_solutions_model import AiSolution
from src.utils.db.db_constants import DB_NAME, MONGO_URI
from src.utils.logger.logger import logger


class DatabaseConnection:
    def __init__(self):
        self.client = None

    async def connect(self):
        try:
            if self.client is None:
                self.client = AsyncIOMotorClient(MONGO_URI)
                await self.client.server_info()
                await init_beanie(
                    database=self.client[DB_NAME],
                    document_models=[AiSolution],
                )

        except Exception as e:
            logger.error(f'Error connecting to database: {e}')
            raise

    async def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None


db_connection = DatabaseConnection()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('DB Connection Lifespan Started')
    await db_connection.connect()
    yield
    await db_connection.close()
