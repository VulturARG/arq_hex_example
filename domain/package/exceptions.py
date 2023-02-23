from typing import Optional


class PackageException(Exception):
    """Base class for all exceptions in this module."""

    MESSAGE: Optional[str] = None

    def __dict__(self):
        pass


class DimensionError(PackageException):
    MESSAGE = "Error in dimensión parameter"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)

