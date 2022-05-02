"""Use cases around the Note entities."""

from dataclasses import dataclass
from typing import List
from .domain import Note
from .domain import NoteRepository

from ..architecture.auth import User


@dataclass
class CreateNoteUseCase:
    """Create a new Note."""

    note_repository: NoteRepository

    def create_note(self, author: User, text: str, tags: List[str]) -> None:
        pass
