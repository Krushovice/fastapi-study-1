from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from core.models import Film


class Genre(Base, IdIntPkMixin):

    title: Mapped[str] = mapped_column(
        String(50),
        index=True,
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    films: Mapped[list["Film"]] = relationship(
        back_populates="genres",
        secondary="film_genre_assoc",
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Genre(id={self.id}, title={self.title!r})"
