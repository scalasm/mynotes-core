"""Unit tests for __main__ module."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import mynotes.__main__ as main


@pytest.fixture
def mock_uvicorn_run(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock instead of actual uvicorn.run() function."""
    return mocker.patch("uvicorn.run", return_value=None)


@pytest.fixture
def mock_config(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock instead of actual mynotes\.port\.config package and
    related variables."""
    mock_config = mocker.patch("mynotes.port.config", return_value=None)

    mock_config.MYNOTES_HTTP_PORT = "8080"
    mock_config.MYNOTES_DEV_MODE = True

    return mock_config


def test_start(mock_uvicorn_run: Mock, mock_config: Mock) -> None:
    """Verify that start() actually calls uvicorn.run()."""
    main.start()

    assert mock_uvicorn_run.call_count == 1


def test_root() -> None:
    """Tests that root() just returns an informative JSON."""
    root_response = main.root()

    root_response["message"].startswith("MyNotes REST API")
