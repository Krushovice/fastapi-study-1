from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column


from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin


class FilmGenreAssoc(Base, IdIntPkMixin):
    __tablename__ = "film_genre_assoc"

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
