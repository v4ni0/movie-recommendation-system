"""Application-specific exception hierarchy."""


class AppError(Exception):
    """Base class for all application errors."""


class DataNotFoundError(AppError):
    """Raised when a required data file is missing."""


class IndexNotReadyError(AppError):
    """Raised when the FAISS index cannot be loaded or is empty."""


class InvalidQueryError(AppError):
    """Raised when the user provides an empty or invalid query."""
