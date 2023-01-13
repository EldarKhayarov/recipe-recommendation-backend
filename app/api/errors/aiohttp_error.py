from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from aiohttp.http_exceptions import HttpProcessingError
from loguru import logger


async def aiohttp_processing_error_handler(
    _: Request, exc: HttpProcessingError
) -> JSONResponse:
    logger.warning(f"Error when external service API connection: {exc.message}")
    return JSONResponse(
        {"errors": ["Cannot connect to external services."]},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
