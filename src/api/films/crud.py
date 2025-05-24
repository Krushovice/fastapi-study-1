from api.base_crud import BaseCRUD
from api.films import FilmCreateSchema, FilmUpdateSchema
from core.models import Film


class FilmCRUD(BaseCRUD[Film, FilmCreateSchema, FilmUpdateSchema]):
    model = Film
