import unittest

try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_to_write_01(self) -> None:
        self.assertEqual(
            self.solution.solveProblemName("input here"),
            "expected result",
        )


if __name__ == '__main__':
    unittest.main()