from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin

from fastapi_users.db import SQLAlchemyBaseUserTable


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
