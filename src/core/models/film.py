from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from core.models import Genre


class Film(Base, IdIntPkMixin):

    title: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    genre: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    duration: Mapped[int | None] = mapped_column(
        Integer,
    )
    release_date: Mapped[date | None] = mapped_column(
        Date,
    )

    poster: Mapped[str] = mapped_column(String(120), nullable=True)

    genres: Mapped[list["Genre"]] = relationship(
        back_populates="films",
        secondary="film_genre_assoc",
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.title!r})"
