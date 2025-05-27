from api.base_crud import BaseCRUD
from api.films.schemas import FilmCreateSchema, FilmUpdateSchema
from core.models import Film


class FilmCRUD(BaseCRUD[Film, FilmCreateSchema, FilmUpdateSchema]):
    model = Film
