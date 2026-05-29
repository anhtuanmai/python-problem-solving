import unittest

try:
    from .solution import Solution
except ImportError:
    from solution import Solution


class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_1(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("aA1!"),
            25,
        )
        
    def test_only_lowercase(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("abc"),
            12,
        )

    def test_only_uppercase(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("ABC"),
            15,
        )

    def test_only_digits(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("123"),
            24,
        )

    def test_repeated_same_char(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("aaaa"),
            4,
        )

    def test_mixed_with_repeats(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("aAaA11!!"),
            25,
        )

    def test_empty_string(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength(""),
            0,
        )

    def test_single_symbol(self) -> None:
        self.assertEqual(
            self.solution.passwordStrength("#"),
            8,
        )

if __name__ == '__main__':
    unittest.main()