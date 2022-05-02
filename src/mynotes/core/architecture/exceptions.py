"""Shared architecture elements, like exception management."""

from dataclasses import dataclass


class ApplicationException(Exception):
    """Base class for all application exception."""

    pass


class ValidationException(ApplicationException):
    """Something happened about the required input values."""

    attribute_name: str
    error_message: str


class RepositoryException(ApplicationException):
    """Exception throws because of the errors in the repository layer."""

    pass


@dataclass
class ResourceNotFoundException(RepositoryException):
    """No Resource was found for a given type and id."""

    resource_type: str
    resource_id: str | int
