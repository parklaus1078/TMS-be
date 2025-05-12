import pytest

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.ai_solutions.ai_solutions_model import AiSolution


@pytest.fixture()
def get_client():
    return AsyncIOMotorClient('mongodb://localhost:27017')


@pytest.fixture()
async def init_test_db(get_client):
    client = get_client
    mock_tms_backend_db = client['mock_tms_backend_db']
    try:
        await client.drop_database('mock_tms_backend_db')
        await init_beanie(database=mock_tms_backend_db, document_models=[AiSolution])
        yield client
    finally:
        await client.drop_database('mock_tms_backend_db')
        client.close()


@pytest.fixture()
async def set_up_data(init_test_db):
    for i in range(10):
        await AiSolution(
            name=f'test {i}',
            keywords=[f'test keyword {j}' for j in range(i)],
            provider=f'test provider {i}',
            url=f'test url {i}',
            thumbnail=f'test thumbnail {i}' if i % 2 == 0 else None,
        ).save()
