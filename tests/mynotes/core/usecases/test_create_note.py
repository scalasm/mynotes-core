"""Tests for create note usecase."""
import datetime
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from mynotes.core.domain.entities import Note
from mynotes.core.domain.entities import NoteRepository
from mynotes.core.domain.entities import NoteType
from mynotes.core.usecases.create_note import CreateNoteRequest
from mynotes.core.usecases.create_note import CreateNoteUseCase

TEST_NOTE_ID = "test_id"


DEFAULT_NOW = datetime.datetime(2022, 5, 1)


@pytest.fixture
def mock_now(module_mocker: MockerFixture) -> Mock:
    """Mock the date and time used in the use case."""
    return module_mocker.patch(
        "mynotes.core.usecases.create_note.now", return_value=DEFAULT_NOW
    )


@pytest.fixture
def mock_note_repository(mocker: MockerFixture) -> Mock:
    """Mock repository dependency."""
    return mocker.Mock(spec=NoteRepository)


@pytest.fixture
def usecase(mock_note_repository: Mock) -> CreateNoteUseCase:
    """Create the SUT."""
    return CreateNoteUseCase(note_repository=mock_note_repository)


def _fake_save_note(note: Note) -> Note:
    saved_note = note.copy()
    saved_note.id = TEST_NOTE_ID
    return saved_note


class TestCreateNoteUseCase:
    """Unit tests for CreateNoteUseCase."""

    def test_should_create_note_if_valid_input(
        self,
        usecase: CreateNoteUseCase,
        mock_note_repository: Mock,
        mock_now: Mock,
    ) -> None:
        """Test that the use case works correctly."""
        test_request = CreateNoteRequest(
            author="test_user", text="This is a test", tags=["test"]
        )

        mock_note_repository.save.side_effect = _fake_save_note

        response = usecase.create_note(test_request)

        mock_note_repository.save.assert_called_once_with(
            Note(
                author_id="test_user",
                creation_time=mock_now(),
                text="This is a test",
                type=NoteType.FREE,
                tags=["test"],
            )
        )

        assert response.note_id == TEST_NOTE_ID
