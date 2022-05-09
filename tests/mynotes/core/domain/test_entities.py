"""Tests for domain entities."""
import datetime
from typing import List
from typing import Optional
from typing import Tuple

import pytest
from pydantic.error_wrappers import ValidationError

from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteType

DEFAULT_NOW = datetime.datetime(2022, 5, 1)

test_note_creation_data = [
    (None, "text", "some_author", NoteType.FREE, DEFAULT_NOW, ["test"]),
    (None, "text", "some_author", NoteType.FREE, DEFAULT_NOW, []),
    (None, "text", "some_author", NoteType.FREE, DEFAULT_NOW, ["test1", "test2"]),
    ("fake_id", "text", "some_author", NoteType.FREE, DEFAULT_NOW, ["test1", "test2"]),
]


@pytest.mark.parametrize(
    "id,text,author_id,type,creation_time,tags", test_note_creation_data
)
def test_note_creation(
    id: Optional[str],
    text: str,
    author_id: str,
    type: NoteType,
    creation_time: datetime.datetime,
    tags: List[str],
) -> None:
    """Test that we can create a note if inputs are correct."""
    new_note = Note(
        id=id,
        text=text,
        author_id=author_id,
        type=type,
        creation_time=creation_time,
        tags=tags,
    )

    assert new_note.id == id
    assert new_note.text == text
    assert new_note.type == type
    assert new_note.creation_time == creation_time
    assert new_note.tags == tags


test_note_creation_validation_errors_data: List[
    Tuple[
        Optional[str],
        Optional[str],
        Optional[str],
        Optional[NoteType],
        Optional[datetime.datetime],
        Optional[List[str]],
        int,
    ]
] = [
    (None, None, None, None, None, None, 5),
    (None, None, "some_author", NoteType.FREE, DEFAULT_NOW, ["test"], 1),
    (None, "test", None, NoteType.FREE, DEFAULT_NOW, ["test"], 1),
    (None, "test", "some_author", NoteType.FREE, None, ["test"], 1),
    (None, "test", None, None, DEFAULT_NOW, None, 3),
    (None, None, None, None, None, [], 4),
]


@pytest.mark.parametrize(
    "id,text,author_id,type,creation_time,tags,expected_num_errors",
    test_note_creation_validation_errors_data,
)
def test_note_creation_validation_errors(
    id: Optional[str],
    text: str,
    author_id: str,
    type: NoteType,
    creation_time: datetime.datetime,
    tags: List[str],
    expected_num_errors: int,
) -> None:
    """Test that we catch the validation errors when creating notes incorrectly."""
    with pytest.raises(ValidationError) as exception_info:
        Note(
            id=id,
            text=text,
            author_id=author_id,
            type=type,
            creation_time=creation_time,
            tags=tags,
        )

    assert len(exception_info.value.errors()) == expected_num_errors
