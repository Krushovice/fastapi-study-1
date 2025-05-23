import uvicorn

from api import films_router
from core import settings
from create_app import create_app


app = create_app()
app.include_router(films_router)


@app.get(
    "/",
    tags=["main"],
    summary="Главная страница",
)
def index():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run(
        "app",
        host=settings.app.host,
        port=int(settings.app.port),
        reload=settings.app.reload,
    )
