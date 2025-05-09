from src.ai_solutions.ai_solutions_model import AiSolutions
from src.ai_solutions.ai_solutions_repository import AiSolutionsRepository


class AiSolutionsService:
    def __init__(self, repository: AiSolutionsRepository):
        self.repository = repository

    async def get_ai_solutions(self) -> list[AiSolutions]:
        return await self.repository.get_ai_solutions()
