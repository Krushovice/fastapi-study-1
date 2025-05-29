from typing import Annotated

from fastapi import APIRouter, Form, Request, HTTPException
from pydantic import BaseModel, EmailStr
from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/users", tags=["Users"])

templates = Jinja2Templates(directory="templates")


class UserCreateSchema(BaseModel):
    # first_name: str
    # username: str
    email: EmailStr
    password: str

    model_config = {"extra": "forbid"}


@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("users/login.html", {"request": request})


@router.post("/login")
async def login(
    data: Annotated[UserCreateSchema, Form()],
):
    if data.email == "test@mail.ru" and data.password == "test":
        return {"success": True, "message": "Login successful!"}
    raise HTTPException(status_code=401, detail="Invalid username or password")
