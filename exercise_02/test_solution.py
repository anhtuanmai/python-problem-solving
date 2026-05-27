import unittest

try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("aA1!"),
            11,
        )

    def test_example_2(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("bbB11#"),
            11,
        )

    def test_only_lowercase_distinct(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("abca"),
            3,
        )

    def test_only_specials_distinct(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("!!@@##$$"),
            20,
        )

    def test_mixed_repeated_characters(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("aAaA111!@"),
            16,
        )


if __name__ == '__main__':
    unittest.main()