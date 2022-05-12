"""Unit tests for architecture utils module."""
from typing import Any
from typing import Dict

import pytest

from mynotes.core.architecture.utils import decode_str_as_dict
from mynotes.core.architecture.utils import encode_dict_to_base64


SAMPLE_CONTINUATION_TOKEN = {
    "creation_time": {"S": "2022-03-23T22:02:36.233752+0000"},
    "author_id_and_type": {"S": "__PUBLIC__#F"},
    "id": {"S": "1"},
}
SAMPLE_CONTINUATION_TOKEN_BASE64 = (
    "eyJjcmVhdGlvbl90aW1lIjogeyJTIjogIjIwMjIt"
    "MDMtMjNUMjI6MDI6MzYuMjMzNzUyKzAwMDAifSwgImF1dGhvcl9pZF9hbmRfdHlwZSI6IHs"
    "iUyI6ICJfX1BVQkxJQ19fI0YifSwgImlkIjogeyJTIjogIjEifX0="
)

test_encode_test_data = [
    (SAMPLE_CONTINUATION_TOKEN, SAMPLE_CONTINUATION_TOKEN_BASE64)
]


@pytest.mark.parametrize(
    "continuation_token_dict,expected_string", test_encode_test_data
)
def test_encode(
    continuation_token_dict: Dict[str, Any], expected_string: str
) -> None:
    """Ensure that encoding works fine."""
    assert encode_dict_to_base64(continuation_token_dict) == expected_string


test_decode_test_data = [
    (SAMPLE_CONTINUATION_TOKEN_BASE64, SAMPLE_CONTINUATION_TOKEN),
    ("", None),
]


@pytest.mark.parametrize(
    "continuation_token_as_base64,expected_token_dict", test_decode_test_data
)
def test_decode(
    continuation_token_as_base64: str, expected_token_dict: Dict[str, Any]
) -> None:
    """Ensure that decoding a string to dictionary works."""
    assert (
        decode_str_as_dict(continuation_token_as_base64) == expected_token_dict
    )
