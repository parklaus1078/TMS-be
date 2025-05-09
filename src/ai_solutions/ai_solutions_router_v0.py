from fastapi import APIRouter, Depends

from src.ai_solutions.ai_solutions_dependency import get_ai_solution_service
from src.ai_solutions.ai_solutions_model import AiSolutions
from src.ai_solutions.ai_solutions_service import AiSolutionsService

router = APIRouter(prefix='/v0/ai-solutions', tags=['ai-solutions'])


@router.get(
    '/',
    summary='Get AI solutions',
    description='Get all AI solutions',
    response_description='A list of AI solutions with name, keywords, provider, url and thumbnail. ',
    response_model=list[AiSolutions],
)
async def get_ai_solutions(
    ai_solutions_service: AiSolutionsService = Depends(get_ai_solution_service),
) -> list[AiSolutions]:
    return await ai_solutions_service.get_ai_solutions()
