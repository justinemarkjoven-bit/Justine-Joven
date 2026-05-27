"""Custom exceptions for library management system."""


class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""

    pass


class MemberNotFoundError(Exception):
    """Raised when a member is not found in the library."""

    pass


class BookUnavailableError(Exception):
    """Raised when a book is already borrowed and cannot be borrowed again."""

    pass


class InvalidInputError(Exception):
    """Raised when invalid input is provided."""

    pass