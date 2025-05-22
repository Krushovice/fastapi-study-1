from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/films", tags=["films"])


films = [
    {
        "id": 1,
        "title": "Оно",
        "genre": "Ужасы",
        "description": "О том как ужасный клоун питается страхом детей",
        "duration": 126,
    },
    {
        "id": 2,
        "title": "Нефть",
        "genre": "драма",
        "description": "О человеке, который поставил нефтяной бизнес выше всего в своей жизни",
        "duration": 158,
    },
    {
        "id": 3,
        "title": "8 миля",
        "genre": "драма",
        "description": "О становлении репера Еминема",
        "duration": 110,
    },
    {
        "id": 4,
        "title": "Всегда говори да!",
        "genre": "комедия",
        "description": "О депрессивном парне , который нашел смысл жизни в мелочах",
        "duration": 135,
    },
]


class Film(BaseModel):
    title: str
    genre: str
    description: str
    duration: int


@router.get("")
def films_index() -> list:
    return films


@router.get("/{film_id}")
def film_detail(film_id: int) -> dict | None:
    for film in films:
        if film["id"] == film_id:
            return film
    raise HTTPException(status_code=404, detail="Film not found")


@router.post("")
def film_create(film_in: Film) -> dict:
    films.append(
        {
            "id": len(films) + 1,
            "title": film_in.title,
            "genre": film_in.genre,
            "description": film_in.description,
            "duration": film_in.duration,
        }
    )
    return {"success": True, "message": "Film created!"}
