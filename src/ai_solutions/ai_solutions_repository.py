from src.ai_solutions.ai_solutions_model import AiSolutions


class AiSolutionsRepository:
    def __init__(self):
        pass

    async def get_ai_solutions(self) -> list[AiSolutions]:
        return await AiSolutions.find_all().to_list()
