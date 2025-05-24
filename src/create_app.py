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
