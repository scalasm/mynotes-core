"""Use cases around the Note entities."""
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from mynotes.core.architecture.data_access import DataPage
from mynotes.core.architecture.data_access import DataPageQuery
from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteRepository
from mynotes.core.domain.entities import NoteType


class FindAllNotesRequest(BaseModel):
    """Request for finding a note by its id."""

    note_type: Optional[NoteType] = Field()
    page_size: int = Field(...)


class FindAllNotesResponse(BaseModel):
    """Response for finding a note by its id."""

    data_page: DataPage[Note]


class FindAllNotesUseCase:
    """Use case for finding a note given its id."""

    _note_repository: NoteRepository

    def __init__(self, note_repository: NoteRepository) -> None:
        """Build this use case.

        Args:
            note_repository: the repository for accessing note entities
        """
        self._note_repository = note_repository

    def find_all_notes(self, request: FindAllNotesRequest) -> FindAllNotesResponse:
        """Create a new note.

        Args:
            request: search criteria.

        Returns:
            the data matching the search criteria
        """
        data_page_query = DataPageQuery(page_size=request.page_size)

        data_page = None

        if request.note_type:
            data_page = self._note_repository.find_all_by_type(
                request.note_type, data_page_query
            )
        else:
            data_page = self._note_repository.find_all(data_page_query)

        return FindAllNotesResponse(data_page=data_page)
