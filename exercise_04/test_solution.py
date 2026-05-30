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
            self.solution.countValidWordOccurrences(["hello wor","ld hello"], ["hello","world","wor"]),
            [2,1,0],
        )


if __name__ == '__main__':
    unittest.main()