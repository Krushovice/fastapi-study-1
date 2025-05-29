from fastapi_users import FastAPIUsers

from api.dependencies.backend import authentication_backend
from api.dependencies.user_manager_dep import get_user_manager
from core.types.user_id import UserIdType
from core.models import User

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
