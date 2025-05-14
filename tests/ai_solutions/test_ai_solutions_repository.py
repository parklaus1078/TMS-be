import pytest

from src.ai_solutions.ai_solutions_repository import AiSolutionsRepository
from src.utils.exceptions.custom_exceptions import DBException


@pytest.fixture()
def ai_solutions_repository():
    return AiSolutionsRepository()


@pytest.mark.asyncio
async def test_get_ai_solutions_success_no_conditions(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(5, 0, None, None, None)

    assert len(docs) == 5


@pytest.mark.asyncio
async def test_get_ai_solutions_success_provider_condition(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, None, 'prov', None)

    assert len(docs) == 10


@pytest.mark.asyncio
async def test_get_ai_solutions_success_name_condition(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, None, None, 'test 1')

    assert len(docs) == 1


@pytest.mark.asyncio
async def test_get_ai_solutions_success_keywords_condition(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], None, None)

    assert len(docs) == 8


@pytest.mark.asyncio
async def test_get_ai_solutions_success_keywords_condition_with_provider(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], 'provider 2', None)
    assert len(docs) == 1

    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], 'vi', None)
    assert len(docs) == 8


@pytest.mark.asyncio
async def test_get_ai_solutions_success_keywords_condition_with_name(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], None, 'test')
    assert len(docs) == 8

    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], None, 'test 2')
    assert len(docs) == 1


@pytest.mark.asyncio
async def test_get_ai_solutions_success_keywords_condition_with_name_and_provider(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], 'provider 2', 'test1')
    assert len(docs) == 0

    docs = await ai_solutions_repository.get_ai_solutions(10, 0, ['test keyword 6', 'test keyword 1'], 'provider 2', 'test 2')
    assert len(docs) == 1


@pytest.mark.asyncio
async def test_get_ai_solutions_success_sort_by_condition(ai_solutions_repository, set_up_data):
    docs = await ai_solutions_repository.get_ai_solutions(10, 0, None, None, None, 'name', -1)

    for i in range(len(docs)):
        assert docs[i].name == f'test {len(docs) - 1 - i}'


@pytest.mark.asyncio
async def test_get_ai_solutions_failure(ai_solutions_repository):
    with pytest.raises(DBException):
        await ai_solutions_repository.get_ai_solutions(10, 0, None, None, None)
