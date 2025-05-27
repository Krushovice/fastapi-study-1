from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column


from core.models.base import Base


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

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Genre(id={self.id}, title={self.title!r})"
