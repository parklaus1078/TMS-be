from beanie.operators import And, In, RegEx

from src.ai_solutions.ai_solutions_model import AiSolution
from src.utils.exceptions.custom_exceptions import DBException
from src.utils.logger.logger import logger


class AiSolutionsRepository:
    def __init__(self):
        pass

    async def get_ai_solutions(self, limit: int, offset: int, keywords: list[str] | None, provider: str | None, name: str | None, sort_by: str | None = None, sort_dir: int = 1) -> list[AiSolution]:
        try:
            conditions = []
            if keywords:
                conditions.append(In(AiSolution.keywords, keywords))
            if provider:
                conditions.append(RegEx(AiSolution.provider, provider, options='i'))
            if name:
                conditions.append(RegEx(AiSolution.name, name, options='i'))

            sort = [(sort_by, sort_dir)] if sort_by else None
            return await AiSolution.find(And(*conditions) if conditions else {}, limit=limit, skip=offset, sort=sort).to_list()

        except Exception as e:
            logger.error(f'Error getting ai solutions: {e}')
            raise DBException('Failed to get list of AI solutions.')
