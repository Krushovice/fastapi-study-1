from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable


from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass

    @classmethod
    async def get_user_db(cls, session: "AsyncSession"):
        yield SQLAlchemyUserDatabase(session, User)
