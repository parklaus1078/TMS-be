import httpx

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from src.utils.exceptions.custom_exceptions import BadRequestException, DBException, ExternalAPIException, NotFoundException
from src.utils.exceptions.exceptions_dto import ErrorDetailDto, ErrorResponseDto
from src.utils.logger.logger import logger


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, *args, **kwargs) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except BadRequestException as e:
            request_info = await self._get_request_info(request)
            logger.error(f'Exception: {e.__class__.__name__} / status_code: {e.status_code} / message: {e.message} / Request: {request_info}')
            return self._create_error_response(e, e.status_code, e.message)
        except DBException as e:
            request_info = await self._get_request_info(request)
            logger.error(f'Exception: {e.__class__.__name__} / status_code: {e.status_code} / message: {e.message} / Request: {request_info}', exc_info=True)
            return self._create_error_response(e, e.status_code, e.message)
        except ExternalAPIException as e:
            request_info = await self._get_request_info(request)
            logger.error(f'Exception: {e.__class__.__name__} / status_code: {e.status_code} / message: {e.message} / Request: {request_info}', exc_info=True)
            return self._create_error_response(e, e.status_code, e.message)
        except NotFoundException as e:
            request_info = await self._get_request_info(request)
            logger.error(f'Exception: {e.__class__.__name__} / status_code: {e.status_code} / message: {e.message} / Request: {request_info}', exc_info=True)
            return self._create_error_response(e, e.status_code, e.message)
        except Exception as e:
            request_info = await self._get_request_info(request)
            logger.error(f'Exception: {e.__class__.__name__} / status_code: {httpx.codes.INTERNAL_SERVER_ERROR} / message: Internal Server Error. / Request: {request_info}')
            return self._create_error_response(e, httpx.codes.INTERNAL_SERVER_ERROR, 'Internal Server Error.')

    async def _get_request_info(self, request: Request) -> dict:
        try:
            body = (await request.body()).decode()
        except (UnicodeDecodeError, Exception):
            body = None

        return {'method': request.method, 'url': str(request.url), 'headers': dict(request.headers), 'query_params': dict(request.query_params), 'body': body}

    def _create_error_response(self, exc, status_code, message=None):
        error_detail = ErrorDetailDto(statusCode=status_code, message=message or exc.message)
        return JSONResponse(status_code=status_code, content=ErrorResponseDto(detail=error_detail).model_dump())
