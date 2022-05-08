"""Use cases around the Note entities."""
from pydantic import BaseModel
from pydantic import Field

from mynotes.core.domain.entities import NoteRepository


class DeleteNoteRequest(BaseModel):
    """Request for deleting a note."""

    note_id: str = Field(...)


class DeleteNoteUseCase:
    """Use case for creating a new note."""

    _note_repository: NoteRepository

    def __init__(self, note_repository: NoteRepository) -> None:
        """Build this use case.

        Args:
            note_repository: the repository for accessing note entities
        """
        self._note_repository = note_repository

    def delete_note(self, request: DeleteNoteRequest) -> None:
        """Delete note.

        Args:
            request: data required to create a new note.

        """
        self._note_repository.delete_by_id(request.note_id)
