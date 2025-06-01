from fastapi import APIRouter

from core import settings
from .dependencies.authentification.backend import authentication_backend
from .fastapi_users_routers_helper import fastapi_users
from .users.schemas import UserRead, UserCreate

router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
)

# /login /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)

# /register
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
