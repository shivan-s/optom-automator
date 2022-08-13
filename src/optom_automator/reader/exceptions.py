"""Exception for Reader module."""


class ReaderError(Exception):
    """Exception for invalid ReadInstruction."""

    def __init__(self, message):
        """Construct class."""
        self.message = message
        super().__init__()
