"""Use cases around the Note entities."""
from typing import List

from pydantic import BaseModel
from pydantic import Field

from mynotes.core.architecture.utils import now
from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteRepository
from mynotes.core.domain.entities import NoteType


class CreateNoteRequest(BaseModel):
    """Request for creating a new note."""

    author: str = Field(...)
    text: str = Field(...)
    tags: List[str] = Field(...)


class CreateNoteResponse(BaseModel):
    """Response to the creation of a note."""

    note_id: str = Field(...)


class CreateNoteUseCase:
    """Use case for creating a new note."""

    _note_repository: NoteRepository

    def __init__(self, note_repository: NoteRepository) -> None:
        """Build this use case.

        Args:
            note_repository: the repository for accessing note entities
        """
        self._note_repository = note_repository

    def create_note(self, request: CreateNoteRequest) -> CreateNoteResponse:
        """Create a new note.

        Args:
            request: data required to create a new note

        Returns:
            the note's id as part of the use case response
        """
        note = Note(
            author_id=request.author,
            creation_time=now(),
            text=request.text,
            type=NoteType.FREE,
            tags=request.tags,
        )

        saved_note = self._note_repository.save(note)

        return CreateNoteResponse(note_id=saved_note.id)
