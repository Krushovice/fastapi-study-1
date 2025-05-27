from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column


from core.models import Base


class FilmGenreAssoc(Base):
    __tablename__ = "film_genre_assoc"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    film_id: Mapped[int] = mapped_column(
        ForeignKey(
            "films.id",
            ondelete="CASCADE",
        ),
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey(
            "genres.id",
            ondelete="CASCADE",
        ),
    )

    __table_args__ = (
        UniqueConstraint(
            film_id,
            genre_id,
        ),
    )
