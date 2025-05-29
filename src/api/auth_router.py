from fastapi import APIRouter

from .dependencies.authentification.backend import authentication_backend
from .fastapi_users_routers_helper import fastapi_users

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
