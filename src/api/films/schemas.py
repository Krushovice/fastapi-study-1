from datetime import date
from typing import Optional

from pydantic import BaseModel, constr


# Film schemas
class FilmBaseSchema(BaseModel):
    title: str
    description: str
    duration: int | None
    release_date: date | None
    poster: str | None

    genres: Optional[list["GenreSchema"]] = None


class FilmCreateSchema(FilmBaseSchema):
    pass


class FilmUpdateSchema(FilmBaseSchema):
    title: str | None = None
    description: str | None = None
    duration: int | None = None
    release_date: date | None = None
    poster: str | None


class FilmSchema(FilmBaseSchema):
    id: int


# Genre schemas
class GenreBaseSchema(BaseModel):
    title: constr(
        min_length=1,
        max_length=20,
        to_lower=True,
    )
    description: str

    films: Optional[list["FilmSchema"]] = None


class GenreSchema(GenreBaseSchema):
    id: int


class GenreCreateSchema(GenreBaseSchema):
    pass


class GenreUpdateSchema(GenreBaseSchema):
    title: str | None = None
    description: str | None = None
