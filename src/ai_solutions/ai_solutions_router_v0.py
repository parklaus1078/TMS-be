from fastapi import APIRouter, Depends, Query

from src.ai_solutions.ai_solutions_dependency import get_ai_solution_service
from src.ai_solutions.ai_solutions_model import AiSolution
from src.ai_solutions.ai_solutions_service import AiSolutionsService

router = APIRouter(prefix='/v0/ai-solutions', tags=['ai-solutions'])


@router.get(
    '',
    summary='Get AI solutions',
    description='Get all AI solutions',
    response_description='A list of AI solutions with name, keywords, provider, url and thumbnail. ',
    response_model=list[AiSolution],
)
async def get_ai_solutions(
    ai_solutions_service: AiSolutionsService = Depends(get_ai_solution_service),
    limit: int = Query(default=15, description='The number of AI solutions to return'),
    offset: int = Query(default=0, description='The number of AI solutions to skip'),
    keywords: list[str] | None = Query(default=None, description='The keywords to filter the AI solutions by'),
    provider: str | None = Query(default=None, description='The provider to filter the AI solutions by'),
    name: str | None = Query(default=None, description='The name to filter the AI solutions by'),
) -> list[AiSolution]:
    return await ai_solutions_service.get_ai_solutions(limit, offset, keywords, provider, name)
