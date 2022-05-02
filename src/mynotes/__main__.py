"""Start up for RESTful API application."""
from typing import Dict
import uvicorn
from fastapi import FastAPI

from .port import config
from .port import notes_api

app = FastAPI()

app.include_router(notes_api.router)


@app.get("/")
def root() -> Dict[str, str]:
    """Displays a simple message for the root path."""
    return {"message": "Hello World from main app"}


def start() -> None:
    """Launched with `poetry run start` at root level."""
    uvicorn.run(
        "mynotes.__main__:app",
        host="localhost",
        port=config.MYNOTES_HTTP_PORT,
        reload=config.MYNOTES_DEV_MODE,
    )  # pragma: no cover


if __name__ == "__main__":
    start()  # pragma: no cover
