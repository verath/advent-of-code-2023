import unittest

from aoc2023 import dec0


class TestDec0(unittest.TestCase):
    def test_part1(self) -> None:
        self.assertEqual(dec0.part1(), "abc")

    def test_part2(self) -> None:
        self.assertEqual(dec0.part2(), "def")


if __name__ == "__main__":
    unittest.main()
