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
            self.solution.count(
                ["hello wor", "ld hello"],
                ["hello", "world", "wor"],
            ),
            [2, 1, 0],
        )

    def test_to_write_02(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["a-b a--b ", "a-", "b"],
                ["a-b", "a", "b"],
            ),
            [2, 1, 1],
        )

    def test_to_write_03(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["-cat dog- mouse"],
                ["cat", "dog", "mouse", "cat-dog"],
            ),
            [1, 1, 1, 0],
        )

    def test_to_write_04(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["one two one  two"],
                ["one", "two", "three"],
            ),
            [2, 2, 0],
        )

    def test_to_write_05(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["a", "-", "b c", "-", "d"],
                ["a-b", "c-d", "a", "b", "cd"],
            ),
            [1, 1, 0, 0, 0],
        )

    def test_to_write_06(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["ab", "--", "cd", " - ", "ef"],
                ["ab", "cd", "ef", "ab-cd"],
            ),
            [1, 1, 1, 0],
        )

    def test_to_write_07(self) -> None:
        self.assertEqual(
            self.solution.count(
                [" -- ", "-", " - "],
                ["a", "a-b", "z"],
            ),
            [0, 0, 0],
        )

    def test_to_write_08(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["x-y x-yz xy-z x-y"],
                ["x-y", "x-yz", "xy-z", "x", "y", "x-z"],
            ),
            [2, 1, 1, 0, 0, 0],
        )

    def test_to_write_09(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["-a b- c -d- e"],
                ["a", "b", "c", "d", "e", "a-b"],
            ),
            [1, 1, 1, 1, 1, 0],
        )

    def test_to_write_10(self) -> None:
        self.assertEqual(
            self.solution.count(
                ["ab", "-", "cd ef", "-", "g -- h", "-", "i j-", "k"],
                ["ab-cd", "ef-g", "h-i", "j-k", "ab", "cd", "h", "i", "ef", "g"],
            ),
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        )


if __name__ == '__main__':
    unittest.main()