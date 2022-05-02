"""Shared architecture elements, like exception management."""
from dataclasses import dataclass


class ApplicationError(Exception):
    """Base class for all application exception."""

    pass


class ValidationError(ApplicationError):
    """Something happened about the required input values."""

    attribute_name: str
    error_message: str


class RepositoryError(ApplicationError):
    """Exception throws because of the errors in the repository layer."""

    pass


@dataclass
class ResourceNotFoundError(RepositoryError):
    """No Resource was found for a given type and id."""

    resource_type: str
    resource_id: str
