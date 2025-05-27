from datetime import date

from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Film(Base):

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

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

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.title!r})"
