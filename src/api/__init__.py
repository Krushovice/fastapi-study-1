__app__ = (
    "router",
    "BaseCRUD",
)

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from api.films.router import router as films_router
from api.users.router import router as users_router
from core import settings
from .auth_router import router as auth_router

from api.base_crud import BaseCRUD

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(films_router)
router.include_router(users_router)

router.include_router(auth_router)
