"""Authentication domain."""
from dataclasses import dataclass


@dataclass
class User:
    """A user within the system."""

    user_id: str
