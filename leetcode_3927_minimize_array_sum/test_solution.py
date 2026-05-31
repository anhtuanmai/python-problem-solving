import unittest

try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_01(self) -> None:
        self.assertEqual(
            self.solution.solve([3, 6, 2]),
            7,
        )

    def test_02(self) -> None:
        self.assertEqual(
            self.solution.solve([4, 2, 8, 3]),
            9,
        )

    def test_03(self) -> None:
        self.assertEqual(
            self.solution.solve([7, 5, 9]),
            21,
        )

    def test_04(self) -> None:
        self.assertEqual(
            self.solution.solve([1, 10, 100]),
            3,
        )

    def test_05(self) -> None:
        self.assertEqual(
            self.solution.solve([5]),
            5,
        )

    def test_06(self) -> None:
        self.assertEqual(
            self.solution.solve([2, 2, 2, 2]),
            8,
        )

    def test_07(self) -> None:
        self.assertEqual(
            self.solution.solve([6, 3, 12, 9]),
            12,
        )

    def test_08(self) -> None:
        self.assertEqual(
            self.solution.solve([8, 4, 2, 16]),
            8,
        )

    def test_09(self) -> None:
        self.assertEqual(
            self.solution.solve([6, 10, 15]),
            31,
        )

    def test_10(self) -> None:
        self.assertEqual(
            self.solution.solve([3, 3, 9, 27, 6]),
            15,
        )


if __name__ == '__main__':
    unittest.main()