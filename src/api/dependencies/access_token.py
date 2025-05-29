from typing import Annotated, TYPE_CHECKING

from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase

from core import db_helper

if TYPE_CHECKING:
    from core.models import AccessToken
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
