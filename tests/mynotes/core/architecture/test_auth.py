"""Tests for the auth module."""
from mynotes.core.architecture.auth import User

import pytest

# Note that I could have done just a pragma no cover for the User class
# but I leave this here as an example.
test_create_user_data = [(None, None), ("mario", "mario")]


@pytest.mark.parametrize("user_id,expected_user_id", test_create_user_data)
def test_create_user(user_id: str, expected_user_id: str) -> None:
    """Test that User instances are created correctly."""
    test_user = User(user_id=user_id)
    assert test_user.user_id == expected_user_id
