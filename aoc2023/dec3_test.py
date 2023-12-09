import unittest

from aoc2023 import common, dec3

PART1_EXAMPLE_INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".lstrip()

PART2_EXAMPLE_INPUT = PART1_EXAMPLE_INPUT


class TestDec3(unittest.TestCase):
    def test_parse_number(self) -> None:
        num_val, num_len = dec3.parse_number("123.")
        self.assertEqual(num_val, 123)
        self.assertEqual(num_len, 3)

    def test_parse_line(self) -> None:
        y = 0
        line = "617*......"
        expected_numbers = [dec3.Number((0, 0), (2, 0), 617)]
        expected_symbols = {(3, 0): "*"}
        actual_numbers, actual_symbols = dec3.parse_line(y, line)
        self.assertEqual(expected_numbers, actual_numbers)
        self.assertEqual(expected_symbols, actual_symbols)

    def test_parse_schematic(self) -> None:
        input = "467..114..\n...*......"
        expected_numbers = [
            dec3.Number((0, 0), (2, 0), 467),
            dec3.Number((5, 0), (7, 0), 114),
        ]
        expected_symbols = {(3, 1): "*"}
        actual_numbers, actual_symbols = dec3.parse_schematic(input)
        self.assertEqual(expected_numbers, actual_numbers)
        self.assertEqual(expected_symbols, actual_symbols)

    def test_part1_example(self) -> None:
        expected = 4361
        actual = dec3.part1(PART1_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    def test_part1(self) -> None:
        expected = 527144
        actual = dec3.part1(common.read_input_text("dec3"))
        self.assertEqual(expected, actual)

    @unittest.skip("NYI")
    def test_part2_example(self) -> None:
        expected = 467835
        actual = dec3.part2(PART2_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    @unittest.skip("NYI")
    def test_part2(self) -> None:
        expected = 0
        actual = dec3.part2(common.read_input_text("dec3"))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
