__app__ = (
    "router",
    "BaseCRUD",
)

from fastapi import APIRouter

from api.films.router import router as films_router
from api.users.router import router as users_router
from core import settings
from .auth_router import router as auth_router

from api.base_crud import BaseCRUD

router = APIRouter(prefix=settings.api.prefix)

router.include_router(films_router)
router.include_router(users_router)

router.include_router(auth_router)
