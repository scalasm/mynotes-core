"""Notes API endpoints."""

import uuid
from fastapi import APIRouter
from fastapi import Depends

from mynotes.core.notes.domain import Note
from mynotes.core.notes.domain import NoteType

from mynotes.core.architecture.utils import now

from .dependencies import get_token_header

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

STUB_NOTE = Note(
    id="1",
    text="This is a new note",
    author_id="Mario",
    type=NoteType.FREE,
    creation_time=now(),
    tags=["test", "stub"],
    version=1,
)

all_notes = {"1": STUB_NOTE}


@router.get("/{note_id}")
async def get_note(note_id: str):
    note = all_notes.get(note_id, None)

    results = {"note_id": note.id, "item": note}
    return results


@router.get("/")
async def get_all_notes():
    results = {"notes": list(all_notes.values)}
    return results


@router.post("/")
async def post(note: Note):
    note.id = uuid.uuid4()

    all_notes[note.id] = note

    results = {"note_id": note.id, "item": STUB_NOTE}
    return results
