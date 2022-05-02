"""Notes API endpoints."""
import uuid

from fastapi import APIRouter

from mynotes.core.architecture.utils import now
from mynotes.core.notes.domain import Note
from mynotes.core.notes.domain import NoteType

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
    """Get a single note by id.

    Args:
        note_id: the id for the note

    Returns:
        the single Note object mathing the requested id
    """
    return all_notes.get(note_id, None)


@router.get("/")
async def get_all_notes():
    """Get all notes.

    Returns:
        a list of Note objects
    """
    results = list(all_notes.values)
    return {"items": results, "size": len(results)}


@router.post("/")
async def post(note: Note):
    """Create a new note (an ID will automatically be assigned).

    Args:
        note: the note to create

    Returns:
        the updated note.
    """
    note.id = uuid.uuid4()

    all_notes[note.id] = note

    return note
