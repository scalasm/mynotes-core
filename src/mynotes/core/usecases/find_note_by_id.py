"""Use cases around the Note entities."""
from pydantic import BaseModel
from pydantic import Field

from mynotes.core.architecture.exceptions import ResourceNotFoundError
from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteRepository


class FindNoteByIdRequest(BaseModel):
    """Request for finding a note by its id."""

    id: str = Field(...)


class FindNoteByIdResponse(BaseModel):
    """Response for finding a note by its id."""

    note: Note = Field(...)


class FindNoteByIdUseCase:
    """Use case for finding a note given its id."""

    _note_repository: NoteRepository

    def __init__(self, note_repository: NoteRepository) -> None:
        """Build this use case.

        Args:
            note_repository: the repository for accessing note entities
        """
        self._note_repository = note_repository

    def find_by_id(self, request: FindNoteByIdRequest) -> FindNoteByIdResponse:
        """Create a new note.

        Args:
            request: data required to create a new note.

        Returns:
            the note, if present

        Raises:
            ResourceNotFoundError: if no such note was found
        """
        note = self._note_repository.find_by_id(request.id)
        if not note:
            raise ResourceNotFoundError(
                resource_type="Note", resource_id=request.id
            )

        return FindNoteByIdResponse(note=note)
