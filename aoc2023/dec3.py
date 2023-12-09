import dataclasses

from . import common

Coordinate = tuple[int, int]
SymbolLookup = dict[Coordinate, str]


@dataclasses.dataclass
class Number:
    start_coord: Coordinate
    end_coord: Coordinate
    value: int


Schematic = tuple[list[Number], SymbolLookup]


def is_part_number(number: Number, symbols: SymbolLookup) -> bool:
    start_x = max(0, number.start_coord[0] - 1)
    end_x = number.end_coord[0] + 1
    start_y = max(0, number.start_coord[1] - 1)
    end_y = number.end_coord[1] + 1

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if (x, y) in symbols:
                return True

    return False


def parse_number(s: str) -> tuple[int, int]:
    val = s[0]
    s = s[1:]
    while s and s[0] in "0123456789":
        val += s[0]
        s = s[1:]
    return int(val), len(val)


def parse_line(y: int, line: str) -> Schematic:
    numbers: list[Number] = []
    symbols: SymbolLookup = {}
    x = 0
    while line:
        ch = line[0]
        num_chars = 1
        if ch in "0123456789":
            value, num_chars = parse_number(line)
            start_coord = (x, y)
            end_coord = (x + num_chars - 1, y)
            numbers.append(Number(start_coord, end_coord, value))
        elif ch != ".":
            symbols[x, y] = ch
        x += num_chars
        line = line[num_chars:]
    return numbers, symbols


def parse_schematic(s: str) -> Schematic:
    schematic_numbers: list[Number] = []
    schematic_symbols: SymbolLookup = {}
    for line_index, line in enumerate(s.splitlines()):
        numbers, symbols = parse_line(line_index, line)
        schematic_numbers.extend(numbers)
        schematic_symbols.update(symbols)
    return schematic_numbers, schematic_symbols


def part1(input: str) -> int:
    numbers, symbols = parse_schematic(input)
    part_numbers = [n.value for n in numbers if is_part_number(n, symbols)]
    return sum(part_numbers)


def part2(input: str) -> int:
    raise NotImplementedError()


def main() -> None:
    input = common.read_input_text("dec3")
    print("part1=", part1(input))
    print("part2=", part2(input))


if __name__ == "__main__":
    main()
