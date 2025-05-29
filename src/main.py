import uvicorn
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api import router as main_router
from core import settings
from create_app import create_app


app = create_app()
app.include_router(main_router)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get(
    "/",
    tags=["main"],
    summary="Главная страница",
    include_in_schema=False,
)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


if __name__ == "__main__":
    uvicorn.run(
        "app",
        host=settings.app.host,
        port=int(settings.app.port),
        reload=settings.app.reload,
    )
