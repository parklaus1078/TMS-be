from src.ai_solutions.ai_solutions_repository import AiSolutionsRepository
from src.ai_solutions.ai_solutions_service import AiSolutionsService


def get_ai_solution_service():
    return AiSolutionsService(get_ai_solution_repository())


def get_ai_solution_repository():
    return AiSolutionsRepository()
