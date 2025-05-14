from fastapi import status


class BaseException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


class DBException(BaseException):
    def __init__(self, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, message: str = 'Database Error happpened'):
        super().__init__(status_code, message)


class ExternalAPIException(BaseException):
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST, message: str = 'Failed to External API request'):
        super().__init__(status_code, message)


class NotFoundException(BaseException):
    def __init__(self, status_code: int = status.HTTP_404_NOT_FOUND, message: str = 'Not found'):
        super().__init__(status_code, message)


class BadRequestException(BaseException):
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST, message: str = 'Something is wrong with the request(e.g. body, query parameter, etc.)'):
        super().__init__(status_code, message)
