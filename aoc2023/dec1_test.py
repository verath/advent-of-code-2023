import unittest

from aoc2023 import common, dec1

PART1_EXAMPLE_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".lstrip()

PART2_EXAMPLE_INPUT = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".lstrip()


class TestDec1(unittest.TestCase):
    def test_part1_example(self) -> None:
        expected = 142
        actual = dec1.part1(PART1_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    def test_part1(self) -> None:
        expected = 54632
        actual = dec1.part1(common.read_input_text("dec1"))
        self.assertEqual(expected, actual)

    def test_part2_example(self) -> None:
        expected = 281
        actual = dec1.part2(PART2_EXAMPLE_INPUT)
        self.assertEqual(expected, actual)

    def test_transform_line_overlapping(self) -> None:
        line = "2oneight9"
        expected = "2189"
        actual = dec1.transform_line(line)
        self.assertEqual(expected, actual)

    def test_part2(self) -> None:
        expected = 54019
        actual = dec1.part2(common.read_input_text("dec1"))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
