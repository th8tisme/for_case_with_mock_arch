"""Entrypoint for the python -m bot_tg.main invocation."""

from .config import CONFIG
from .handlers import build_report


def main() -> None:
    print("Running as python -m bot_tg.main")
    print(f"config: {CONFIG}")
    print(f"report: {build_report()}")


if __name__ == "__main__":
    main()
