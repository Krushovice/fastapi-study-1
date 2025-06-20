from fastapi import FastAPI

from lifespan import app_lifespan


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=app_lifespan,
        title="My shop",
        description="FastAPI study project",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    return app


# TODO new version app with docs and html response on production
# from contextlib import asynccontextmanager
# from typing import AsyncGenerator
#
# from fastapi import FastAPI
# from fastapi.openapi.docs import (
#     get_redoc_html,
#     get_swagger_ui_html,
#     get_swagger_ui_oauth2_redirect_html,
# )
# from fastapi.responses import ORJSONResponse
# from starlette.responses import HTMLResponse
#
# from api.webhooks import webhooks_router
# from core.models import db_helper
# from errors_handlers import register_errors_handlers
# from middlewares import register_middlewares
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
#     # startup
#     yield
#     # shutdown
#     await db_helper.dispose()
#
#
# def register_static_docs_routes(app: FastAPI) -> None:
#     @app.get("/docs", include_in_schema=False)
#     async def custom_swagger_ui_html() -> HTMLResponse:
#         return get_swagger_ui_html(
#             openapi_url=str(app.openapi_url),
#             title=app.title + " - Swagger UI",
#             oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#             swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
#             swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
#         )
#
#     @app.get(str(app.swagger_ui_oauth2_redirect_url), include_in_schema=False)
#     async def swagger_ui_redirect() -> HTMLResponse:
#         return get_swagger_ui_oauth2_redirect_html()
#
#     @app.get("/redoc", include_in_schema=False)
#     async def redoc_html() -> HTMLResponse:
#         return get_redoc_html(
#             openapi_url=str(app.openapi_url),
#             title=app.title + " - ReDoc",
#             redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
#         )
#
#
# def create_app(
#     create_custom_static_urls: bool = False,
# ) -> FastAPI:
#     app = FastAPI(
#         default_response_class=ORJSONResponse,
#         lifespan=lifespan,
#         docs_url=None if create_custom_static_urls else "/docs",
#         redoc_url=None if create_custom_static_urls else "/redoc",
#         webhooks=webhooks_router,
#     )
#     if create_custom_static_urls:
#         register_static_docs_routes(app)
#
#     register_errors_handlers(app)
#     register_middlewares(app)
#     return app
