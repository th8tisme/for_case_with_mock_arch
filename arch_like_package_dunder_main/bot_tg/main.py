"""Logic reused by the __main__ entrypoint."""

from .config import CONFIG
from .handlers import format_summary


def main() -> None:
    print("Running as python -m bot_tg")
    print(f"config: {CONFIG}")
    print(f"summary: {format_summary()}")


if __name__ == "__main__":
    main()
