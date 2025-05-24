from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.db_helper import db_helper


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    yield
    await db_helper.engine.dispose()
