"""Custom logging."""

import logging

from rich.logging import RichHandler

FORMAT = "%(message)s"
LEVEL = logging.INFO

logging.basicConfig(
    level=LEVEL,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()],
)

log = logging.getLogger("rich")
