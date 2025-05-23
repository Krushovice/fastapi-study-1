from datetime import date

from pydantic import BaseModel


class FilmBaseSchema(BaseModel):
    title: str
    genre: str
    description: str
    duration: int
    release_date: date


class FilmCreateSchema(FilmBaseSchema):
    pass


class FilmUpdateSchema(FilmBaseSchema):
    title: str | None = None
    genre: str | None = None
    description: str | None = None
    duration: int | None = None
    release_date: date | None = None


class FilmSchema(FilmBaseSchema):
    id: int
