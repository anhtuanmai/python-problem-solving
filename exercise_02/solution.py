"""
Calculate the strength of a password based on distinct characters.

Scoring rules:
- 1 point for each distinct lowercase letter.
- 2 points for each distinct uppercase letter.
- 3 points for each distinct digit.
- 5 points for each distinct special character from "!@#$".

Each character contributes at most once, even if it appears multiple times.

Args:
    password: A string containing lowercase letters, uppercase letters,
        digits, and special characters from "!@#$".

Returns:
    The total password strength as an integer.

Examples:
    "aA1!" -> 25
    "abc" -> 12
"""


class Solution:

    def passwordStrength(self, password: str) -> int:
        unique_chars = set(password)
        point = 0
        for ch in unique_chars:
                if (ch.islower()):
                    point += 1
                else: 
                    if (ch.isupper()):
                        point += 2
                    else:
                        point += 5
        point += 3* len(unique_chars)

        return point


if __name__ == "__main__":
    import unittest
    from test_solution import TestExercise

    unittest.main()
