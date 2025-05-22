import uvicorn

from create_app import create_app
from core import settings

app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.app.host,
        port=int(settings.app.port),
        reload=settings.app.reload,
    )
