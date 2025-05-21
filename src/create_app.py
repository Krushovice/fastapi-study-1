from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI-Study",
        description="FastAPI study project",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    return app