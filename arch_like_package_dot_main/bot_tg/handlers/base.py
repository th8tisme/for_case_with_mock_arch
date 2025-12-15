"""Composable handler utilities."""

from ..config import CONFIG
from ..keyboards.main_menu import MAIN_MENU_LABEL


def build_report() -> str:
    """Combine configuration with a keyboard label to show import patterns."""
    return f"{MAIN_MENU_LABEL}-{CONFIG}"
