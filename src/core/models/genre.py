from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base


if TYPE_CHECKING:
    from core.models import Film


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

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
