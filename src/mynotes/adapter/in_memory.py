"""Dummy implementation that uses in memory storage just for design purposes."""
import uuid
from typing import Dict
from typing import Optional

from mynotes.core.architecture.data_access import DataPage
from mynotes.core.architecture.data_access import DataPageQuery
from mynotes.core.architecture.utils import now
from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteRepository
from mynotes.core.domain.entities import NoteType

SAMPLE_NOTE_ID = "1"

SAMPLE_NOTE = Note(
    id=SAMPLE_NOTE_ID,
    text="This is a new note",
    author_id="Mario",
    type=NoteType.FREE,
    creation_time=now(),
    tags=["test", "stub"],
)


class InMemoryNoteRepository(NoteRepository):
    """In memory implementation for the Note operations."""

    _note_storage: Dict[str, Note]

    def __init__(self) -> None:
        """Build a new in-memory note repository."""
        self._note_storage = dict[str, Note]()
        self._note_storage[SAMPLE_NOTE_ID] = SAMPLE_NOTE

    def save(self, note: Note) -> Note:
        """Create a new note."""
        saved_note = note.copy()
        saved_note.id = str(uuid.uuid4())

        self._note_storage[saved_note.id] = saved_note
        return saved_note

    def delete_by_id(self, note_id: str) -> None:
        """Delete a note."""
        del self._note_storage[note_id]

    def find_by_id(self, note_id: str) -> Optional[Note]:
        """Find a note by its id."""
        return self._note_storage.get(note_id, None)

    def find_all(self, data_page_query: DataPageQuery) -> DataPage[Note]:
        """Returns all notes."""
        all_notes = list(self._note_storage.values())

        return DataPage(
            continuation_token=None, page_size=len(all_notes), items=all_notes
        )

    def find_all_by_type(
        self, note_type: NoteType, data_page_query: DataPageQuery
    ) -> DataPage[Note]:
        """Find all notes by type."""
        filtered_notes = list(
            filter(
                lambda note: note.type == note_type,
                list(self._note_storage.values()),
            )
        )

        return DataPage(
            continuation_token=None,
            page_size=len(filtered_notes),
            items=filtered_notes,
        )
