"""Notes business logic."""
from abc import ABC
from abc import abstractmethod
from datetime import datetime
from enum import Enum
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from mynotes.core.architecture.data_access import DataPage
from mynotes.core.architecture.data_access import DataPageQuery


class NoteType(Enum):
    """Supported note types (free notes and interview notes)."""

    FREE = "F"
    INTERVIEW = "I"
    QUESTION = "Q"


class Note(BaseModel):
    """Entity class representing metadata associated to a Note entity."""

    id: Optional[str] = Field()
    text: str = Field(...)
    author_id: str = Field(...)
    type: NoteType = Field(...)
    creation_time: datetime = Field(...)
    tags: List[str] = Field(...)


class NoteRepository(ABC):
    """Data access operations for Note entities."""

    @abstractmethod
    def save(self, note: Note) -> Note:
        """Save a note.

        Args:
            note: the note to save

        Returns:
            the updated note with its id set
        """
        pass

    @abstractmethod
    def find_by_id(self, note_id: str) -> Optional[Note]:
        """Find a note by its id.

        Args:
            note_id: the id of the note to find

        Returns
            a valid Note object if such id exists or None otherwise
        """
        pass

    @abstractmethod
    def delete_by_id(self, note_id: str) -> None:
        """Delete a note by its id.

        Note that nothing will happen if such id is not present.

        Args:
            note_id: the id of the note to delete
        """
        pass

    @abstractmethod
    def find_all(self, data_page_query: DataPageQuery) -> DataPage[Note]:
        """Find all notes regardless of their type or any other criteria.

        Args:
            data_page_query: paging data for running the query

        Returns
            a DataPage, eventually empty if no data was found
        """
        pass

    @abstractmethod
    def find_all_by_type(
        self, note_type: NoteType, data_page_query: DataPageQuery
    ) -> DataPage[Note]:
        """Find all notes of the requested type.

        Args:
            note_type: the required note type to search for
            data_page_query: paging data for running the query

        Returns
            a DataPage, eventually empty if no data was found
        """
        pass
