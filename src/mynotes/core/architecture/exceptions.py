"""Shared architecture elements, like exception management."""
from dataclasses import dataclass


class ApplicationError(Exception):  # pragma: no cover
    """Base class for all application exception."""

    pass


@dataclass
class ValidationError(ApplicationError):  # pragma: no cover
    """Something happened about the required input values."""

    attribute_name: str
    error_message: str


@dataclass
class RepositoryError(ApplicationError):  # pragma: no cover
    """Exception throws because of the errors in the repository layer."""

    pass


@dataclass
class ResourceNotFoundError(RepositoryError):  # pragma: no cover
    """No Resource was found for a given type and id."""

    resource_type: str
    resource_id: str


@dataclass
class FeatureNotImplementedError(Exception):  # pragma: no cover
    """Exeception to be used when doing work in progress development."""

    message: str = "<Unknown reason>"
