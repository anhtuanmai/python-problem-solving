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
            self.solution.solveProblemName([1, 1, 1, 2, 2, 3], 2),
            [2, 2, 3],
        )

    def test_02(self) -> None:
        self.assertEqual(
            self.solution.solveProblemName([4, 4, 5], 1),
            [5],
        )


if __name__ == '__main__':
    unittest.main()