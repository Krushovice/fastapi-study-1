from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper


class ModelDepGeneric[TModel]:
    model: TModel

    @classmethod
    async def get_access_token_db(
        cls,
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.session_getter),
        ],
    ):
        yield cls.model.get_db(session=session)
