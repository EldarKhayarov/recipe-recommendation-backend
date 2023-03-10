from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from aiohttp.http_exceptions import HttpProcessingError

from app.core.config import get_app_settings
from app.api.routes.api import router as api_router
from app.api.errors.http_error import http_error_handler
from app.api.errors.aiohttp_error import aiohttp_processing_error_handler
from app.api.errors.validation_error import http422_error_handler


def get_application() -> FastAPI:
    settings = get_app_settings()
    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.add_exception_handler(
        HttpProcessingError, aiohttp_processing_error_handler
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()
