"""Data access abstractions."""
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel


class DataPageQuery(BaseModel):
    """Groups usual query parameters for a set of data."""

    page_size: int = Field(min=1, max=50, default=10)
    continuation_token: Optional[str] = None


# Generic data type per items in a data page
T = TypeVar("T")


class DataPage(GenericModel, Generic[T]):
    """Standard response wrapper from a "find" (query) operation."""

    items: List[T] = []
    page_size: int = 0
    continuation_token: Optional[str] = None
