"""Use cases around the Note entities."""
from dataclasses import dataclass
from typing import List

from mynotes.core.architecture.auth import User
from mynotes.core.notes.domain import NoteRepository


@dataclass
class CreateNoteUseCase:
    """Create a new Note."""

    note_repository: NoteRepository

    def create_note(self, author: User, text: str, tags: List[str]) -> None:
        """Create a new note."""
        pass
