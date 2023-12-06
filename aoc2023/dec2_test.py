import unittest

from aoc2023 import common, dec2

PART1_EXAMPLE_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".lstrip()

PART2_EXAMPLE_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".lstrip()


class TestDec2(unittest.TestCase):
    def test_part1_example(self) -> None:
        expected = 8
        actual = dec2.part1(PART1_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    def test_part1(self) -> None:
        expected = 2727
        actual = dec2.part1(common.read_input_text("dec2"))
        self.assertEqual(expected, actual)

    def test_part2_example(self) -> None:
        expected = 2286
        actual = dec2.part2(PART2_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    def test_part2(self) -> None:
        expected = 56580
        actual = dec2.part2(common.read_input_text("dec2"))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
