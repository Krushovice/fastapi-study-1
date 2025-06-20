from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import (
    DatabaseStrategy,
)

from core import settings
from .access_token import AccessTokenDep

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(AccessTokenDep.get_db),
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_token_db,
        lifetime_seconds=settings.access_token.lt_seconds,
    )
