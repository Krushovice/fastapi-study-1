from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.db_helper import db_helper
from core.models import Film

from .schemas import (
    FilmCreateSchema,
    FilmSchema,
    FilmUpdateSchema,
)
from .crud import FilmCRUD

templates = Jinja2Templates(directory="templates/films")
router = APIRouter(prefix="/films", tags=["films"])


@router.get(
    "",
    response_class=HTMLResponse,
    response_model=List[FilmSchema],
)
async def films_index(
    request: Request,
    session: AsyncSession = Depends(dependency=db_helper.session_getter),
) -> HTMLResponse:

    films = await FilmCRUD.read_all(session)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"films": films},
    )


@router.get("/{film_id}", response_model=FilmSchema)
async def film_detail(
    film_id: int,
    session: AsyncSession = Depends(dependency=db_helper.session_getter),
) -> Film | None:

    film = await FilmCRUD.read(session=session, pk=film_id)
    if film:
        return film
    else:
        raise HTTPException(status_code=404, detail="Film not found")


@router.post("")
async def film_create(
    film_in: FilmCreateSchema,
    session: AsyncSession = Depends(dependency=db_helper.session_getter),
) -> dict:
    film = await FilmCRUD.create(session=session, schema_in=film_in)

    if film:
        return {"success": True, "message": "Film created!"}

    return {"success": False, "message": "Film not created!"}


@router.put("/{film_id}")
async def film_update(
    film_id: int,
    updated_film_in: FilmUpdateSchema,
    session: AsyncSession = Depends(dependency=db_helper.session_getter),
) -> dict:
    update_film = await FilmCRUD.update(
        session=session,
        pk=film_id,
        schema_in=updated_film_in,
    )
    if update_film:
        return {"success": True, "message": "Film updated!"}

    return {"success": False, "message": "Film not updated!"}
