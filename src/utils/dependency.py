from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper


SessionDepends = Annotated[AsyncSession, Depends(db_helper.session_getter)]
