from pydantic import Field

from utils.models.base_model import BaseModel


class AiSolutions(BaseModel):
    name: str = Field(..., description='The name of the AI solution(e.g. "ChatGPT", "Synthesia")')
    keywords: list[str] = Field(..., description='The keywords of the AI solution(e.g. "AI", "video editing", "video generation")')
    provider: str = Field(..., description='The name of the provider of the AI solution(e.g. "OpenAI", "Synthesia")')
    url: str = Field(..., description='The URL of the AI solution provider(e.g. "https://openai.com", "https://synthesia.com")')
    thumbnail: str = Field(..., description='The URL of the thumbnail of the AI solution')
