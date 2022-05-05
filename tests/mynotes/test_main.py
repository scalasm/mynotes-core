"""Unit tests for __main__ module."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import mynotes.__main__ as main


@pytest.fixture
def mock_uvicorn_run(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock instead of actual uvicorn#run() function."""
    return mocker.patch("uvicorn.run", return_value=None)


@pytest.fixture
def stub_http_port(
    mocker: MockerFixture,
) -> int:
    """Provides a stub for MYNOTES_HTTP_PORT."""
    return mocker.patch("mynotes.port.config.MYNOTES_HTTP_PORT", 8080)


@pytest.fixture
def stub_dev_mode(
    mocker: MockerFixture,
) -> bool:
    """Provides a stub for MYNOTES_DEV_MODE."""
    return mocker.patch("mynotes.port.config.MYNOTES_DEV_MODE", True)


def test_start(
    mock_uvicorn_run: Mock, stub_http_port: int, stub_dev_mode: bool
) -> None:
    """Verify that start() actually calls uvicornùrun()."""
    main.start()

    mock_uvicorn_run.assert_called_once_with(
        "mynotes.__main__:app",
        host="localhost",
        port=stub_http_port,
        reload=stub_dev_mode,
    )


def test_root() -> None:
    """Tests that root() just returns an informative JSON."""
    root_response = main.root()

    root_response["message"].startswith("MyNotes REST API")
