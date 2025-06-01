from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from core import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class ModelDepGeneric[TModel]:
    model: TModel

    @classmethod
    async def get_db(
        cls,
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.session_getter),
        ],
    ):
        yield cls.model.get_db(session=session)
