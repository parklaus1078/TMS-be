from pydantic import BaseModel


class ErrorDetailDto(BaseModel):
    statusCode: int
    message: str


class ErrorResponseDto(BaseModel):
    detail: ErrorDetailDto
