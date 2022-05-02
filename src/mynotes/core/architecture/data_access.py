"""Data access abstractions."""
from dataclasses import dataclass
from typing import Generic
from typing import List
from typing import TypeVar


@dataclass
class DataPageQuery:
    """Groups usual query parameters for a set of data."""

    page_size: int = 10
    continuation_token: str | None = None


# Generic data type per items in a data page
T = TypeVar("T")


@dataclass
class DataPage(Generic[T]):
    """Standard response wrapper from a "find" (query) operation."""

    items: List[T]
    page_size: int
    continuation_token: str | None
