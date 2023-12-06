import dataclasses

from . import common


@dataclasses.dataclass
class Cubes:
    red: int
    green: int
    blue: int


@dataclasses.dataclass
class Game:
    id: int
    cubes: list[Cubes]


def parse_cubes(s: str) -> Cubes:
    vals = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for cube in s.split(","):
        cube = cube.strip()
        val, color = cube.split(" ")
        vals[color] += int(val)
    return Cubes(vals["red"], vals["green"], vals["blue"])


def parse_line(s: str) -> Game:
    s = s.removeprefix("Game ")
    game_id, s = s.split(":", 1)
    game_cubes = []
    for cubes_str in s.split(";"):
        game_cubes.append(parse_cubes(cubes_str))
    return Game(int(game_id), game_cubes)


def part1(input: str) -> int:
    possible_game_ids = []
    for line in input.splitlines():
        game = parse_line(line)
        valid = True
        for c in game.cubes:
            valid = valid and (c.red <= 12) and (c.green <= 13) and (c.blue <= 14)
        if valid:
            possible_game_ids.append(game.id)
    return sum(possible_game_ids)


def part2(input: str) -> int:
    cube_powers = []
    for line in input.splitlines():
        game = parse_line(line)
        required_red = 0
        required_green = 0
        required_blue = 0
        for c in game.cubes:
            required_red = max(required_red, c.red)
            required_green = max(required_green, c.green)
            required_blue = max(required_blue, c.blue)
        cube_powers.append(required_red * required_green * required_blue)
    return sum(cube_powers)


def main() -> None:
    input = common.read_input_text("dec2")
    print("part1=", part1(input))
    print("part2=", part2(input))


if __name__ == "__main__":
    main()
