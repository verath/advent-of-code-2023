from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def read_input_text(day: str) -> str:
    return (SCRIPT_DIR / f"{day}_input.txt").read_text()
