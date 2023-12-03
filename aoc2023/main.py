import importlib
import sys


def main() -> None:
    to_run = sys.argv[1:]
    if not to_run:
        to_run = [f"dec{i}" for i in range(0, 31 + 1)]

    for mod_name in to_run:
        try:
            mod = importlib.import_module(f"aoc2023.{mod_name}")
            print(f"# {mod_name}")
            mod.main()
        except ModuleNotFoundError:
            pass


if __name__ == "__main__":
    main()
