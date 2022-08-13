"""Custom exceptions for phrases module."""


class PhrasesError(Exception):
    """Custom Error for Phrase Trees."""

    def __init__(self, value: str, message: str) -> None:
        """Construct exception."""
        self.value = value
        self.message = message
        super().__init__()
