"""Notes business logic."""
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel

from mynotes.core.architecture.data_access import DataPage
from mynotes.core.architecture.data_access import DataPageQuery


class NoteType(Enum):
    """Supported note types (free notes and interview notes)."""

    FREE = "F"
    INTERVIEW = ("I",)
    QUESTION = "Q"


class Note(BaseModel):
    """Entity class representing metadata associated to a Note entity."""

    id: str
    text: str
    author_id: str
    type: NoteType
    creation_time: datetime
    tags: List[str]
    version: int


class NoteRepository(ABC):
    """Data access operations for Note entities."""

    @abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        pass

    @abstractmethod
    def find_all_by_type(
        self, note_type: NoteType, data_page_query: DataPageQuery
    ) -> DataPage[Note]:
        pass
