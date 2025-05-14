from src.ai_solutions.ai_solutions_model import AiSolution
from src.ai_solutions.ai_solutions_repository import AiSolutionsRepository


class AiSolutionsService:
    def __init__(self, repository: AiSolutionsRepository):
        self.repository = repository

    async def get_ai_solutions(self, limit: int, offset: int, keywords: list[str] | None, provider: str | None, name: str | None, sort_by: str | None = None, sort_dir: int = 1) -> list[AiSolution]:
        if sort_dir not in [-1, 1]:
            raise ValueError('sort_dir must be -1 or 1')

        return await self.repository.get_ai_solutions(limit, offset, keywords, provider, name, sort_by, sort_dir)
