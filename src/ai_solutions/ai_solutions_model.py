from pydantic import Field
from pymongo.operations import IndexModel

from src.utils.models.base_model import BaseModel


class AiSolution(BaseModel):
    name: str = Field(..., description='The name of the AI solution(e.g. "ChatGPT", "Synthesia")')
    keywords: list[str] = Field(..., description='The keywords of the AI solution(e.g. "AI", "video editing", "video generation")')
    provider: str = Field(..., description='The name of the provider of the AI solution(e.g. "OpenAI", "Synthesia")')
    url: str = Field(..., description='The URL of the AI solution provider(e.g. "https://openai.com", "https://synthesia.com")')
    thumbnail: str | None = Field(default=None, description='The URL of the thumbnail of the AI solution')

    class Settings:
        name = 'ai_solutions'
        indexes = [IndexModel(keys=[('updated_at', 1)], name='ASC_updated_at')]
