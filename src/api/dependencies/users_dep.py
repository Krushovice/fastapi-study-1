from typing import Annotated, TYPE_CHECKING

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core import db_helper

if TYPE_CHECKING:
    from core.models import User
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield SQLAlchemyUserDatabase(session, User)
