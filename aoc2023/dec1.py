from . import common


def line_value(line: str) -> int:
    first_num = ""
    last_num = ""
    for char in line:
        if char in "123456789":
            first_num = first_num if first_num else char
            last_num = char
    return int(f"{first_num}{last_num}")


def transform_line(line: str) -> str:
    lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    out = ""
    while line:
        if line[0] in "123456789":
            # Single digit, keep.
            out += line[0]
        else:
            # Digit in text form?
            for search, replace in lookup.items():
                if line.startswith(search):
                    out += replace
                    break
        line = line[1:]
    return out


def part1(input: str) -> int:
    sum = 0
    for line in input.splitlines():
        sum += line_value(line)
    return sum


def part2(input: str) -> int:
    sum = 0
    for line in input.splitlines():
        sum += line_value(transform_line(line))
    return sum


def main() -> None:
    input = common.read_input_text("dec1")
    print("part1=", part1(input))
    print("part2=", part2(input))


if __name__ == "__main__":
    main()
