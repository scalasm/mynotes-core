"""Notes API endpoints."""
from typing import Optional

from fastapi import APIRouter

from mynotes.adapter.in_memory import InMemoryNoteRepository
from mynotes.core.architecture.data_access import DataPage
from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteType
from mynotes.core.usecases.create_note import CreateNoteRequest
from mynotes.core.usecases.create_note import CreateNoteResponse
from mynotes.core.usecases.create_note import CreateNoteUseCase
from mynotes.core.usecases.find_all_notes import FindAllNotesRequest
from mynotes.core.usecases.find_all_notes import FindAllNotesUseCase
from mynotes.core.usecases.find_note_by_id import FindNoteByIdRequest
from mynotes.core.usecases.find_note_by_id import FindNoteByIdUseCase

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

note_repository = InMemoryNoteRepository()


@router.on_event("startup")
def initialize_system() -> None:
    """Initialize system at startup."""
    # TODO Initialize things here
    pass


find_by_id_usecase = FindNoteByIdUseCase(note_repository=note_repository)


@router.get("/{note_id}")
async def get_note(note_id: str) -> Optional[Note]:
    """Get a single note by id.

    Args:
        note_id: the id for the note

    Returns:
        the single Note object mathing the requested id
    """
    return find_by_id_usecase.find_by_id(FindNoteByIdRequest(id=note_id)).note


find_all_notes_usecase = FindAllNotesUseCase(note_repository=note_repository)


@router.get("/")
async def get_all_notes(
    note_type: NoteType = None, page_size: int = 10
) -> DataPage[Note]:
    """Get all notes.

    Args:
        note_type: (Query parameter) optional note type for filtering
        page_size: (Query parameter) optional size for the amount of data

    Returns:
        a DataPage containing the Note objects
    """
    result = find_all_notes_usecase.find_all_notes(
        FindAllNotesRequest(note_type=note_type, page_size=page_size)
    )

    return result.data_page


create_note_usecase = CreateNoteUseCase(note_repository=note_repository)


@router.post("/")
async def create_note(request: CreateNoteRequest) -> CreateNoteResponse:
    """Create a new note (an ID will automatically be assigned).

    Args:
        request: Note creation request.

    Returns:
        the created note reference
    """
    return create_note_usecase.create_note(request)
