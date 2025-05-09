from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.ai_solutions.ai_solutions_model import AiSolutions
from src.utils.db.db_constants import DB_NAME, MONGO_URI


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
                    document_models=[AiSolutions],
                )

        except Exception as e:
            print(f'Error connecting to database: {e}')
            raise

    async def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None


db_connection = DatabaseConnection()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('DB Connection Lifespan Started')
    await db_connection.connect()
    yield
    await db_connection.close()
