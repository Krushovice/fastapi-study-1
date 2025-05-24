__app__ = (
    "films_router",
    "BaseCRUD",
)


from .films.router import router as films_router
from .base_crud import BaseCRUD
