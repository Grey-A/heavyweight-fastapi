"""This module contains common types used in the application."""

from typing import NamedTuple


class PaginationParams(NamedTuple):
    """The pagination parameters for the application."""

    page: int
    size: int
