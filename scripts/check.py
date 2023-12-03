import argparse
import logging
import subprocess
import sys
from pathlib import Path

LOGGER = logging.getLogger(__name__)
PYTHON = sys.executable

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
LIB_DIR = PROJECT_DIR / "aoc2023"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="Try to fix issues.")
    return parser.parse_args()


def _run(cmd: list[str], name: str) -> None:
    LOGGER.info(f"{name}: Running...")
    LOGGER.debug(cmd)
    try:
        subprocess.run(cmd, check=True, cwd=PROJECT_DIR)
    except subprocess.CalledProcessError as e:
        LOGGER.error(f"{name}: Failed with exitcode {e.returncode}!")
        sys.exit(e.returncode)
    LOGGER.info(f"{name}: Done")


def _run_black(fix: bool) -> None:
    cmd = ["black", str(PROJECT_DIR), "--extend-exclude=venv"]
    if not fix:
        cmd.extend(["--check", "--diff"])
    _run(cmd, "black")


def _run_flake8() -> None:
    cmd = ["flake8"]
    _run(cmd, "flake8")


def _run_isort(fix: bool) -> None:
    cmd = ["isort", str(PROJECT_DIR), "--profile", "black"]
    if not fix:
        cmd.extend(["--check", "--diff"])
    _run(cmd, "isort")


def _run_mypy() -> None:
    cmd = ["mypy", str(PROJECT_DIR)]
    _run(cmd, "mypy")


def _run_tests() -> None:
    cmd = [
        PYTHON,
        "-m",
        "unittest",
        "discover",
        "--pattern",
        "*_test.py",
        "--start-directory",
        str(LIB_DIR),
    ]
    _run(cmd, "tests")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    )
    args = _parse_args()
    _run_black(args.fix)
    _run_flake8()
    _run_isort(args.fix)
    _run_mypy()
    _run_tests()


if __name__ == "__main__":
    main()
