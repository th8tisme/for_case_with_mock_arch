"""Reusable handler logic for the __main__ example."""

from ..config import CONFIG
from ..keyboards.register import REGISTER_LABEL


def format_summary() -> str:
    """Return a short message that shows imports inside the package."""
    return f"{REGISTER_LABEL}-{CONFIG}"
