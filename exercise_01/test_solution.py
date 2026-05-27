# exercise_01/test_solution.py
import unittest

from .solution import Solution


class TestExercise01(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(
            self.solution.limitOccurrences([1, 1, 1, 2, 2, 3], 2),
            [1, 1, 2, 2, 3],
        )

    def test_example_2(self) -> None:
        self.assertEqual(
            self.solution.limitOccurrences([1, 2, 3], 1),
            [1, 2, 3],
        )

    def test_single_value(self) -> None:
        self.assertEqual(
            self.solution.limitOccurrences([5], 1),
            [5],
        )

    def test_keep_three(self) -> None:
        self.assertEqual(
            self.solution.limitOccurrences([2, 2, 2, 2], 3),
            [2, 2, 2],
        )

    def test_mixed_groups(self) -> None:
        self.assertEqual(
            self.solution.limitOccurrences([1, 1, 2, 2, 2, 3, 3], 2),
            [1, 1, 2, 2, 3, 3],
        )


if __name__ == '__main__':
    unittest.main()