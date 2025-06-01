from fastapi import APIRouter

from starlette.templating import Jinja2Templates

from api.fastapi_users_routers_helper import fastapi_users
from api.users.schemas import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

templates = Jinja2Templates(directory="templates")

# /me /{id}
router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    )
)
