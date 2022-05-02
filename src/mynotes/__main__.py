"""Start up for RESTful API application."""
import uvicorn
from fastapi import FastAPI

from .port import config
from .port import notes_api

app = FastAPI()

app.include_router(notes_api.router)


@app.get("/")
def root():
    return {"message": "Hello World from main app"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run(
        "mynotes.__main__:app",
        host="0.0.0.0",
        port=config.MYNOTES_HTTP_PORT,
        reload=config.MYNOTES_DEV_MODE,
    )  # pragma: no cover


if __name__ == "__main__":
    start(prog_name="mynotes-core")  # pragma: no cover
