"""
Remove all values that appear more than k times.

Problem:
You are given a sorted integer array nums and an integer k.
Return an array containing only elements whose total frequency is less than or equal to k.

Examples:
- nums = [1, 1, 1, 2, 2, 3], k = 2 -> [2, 2, 3]
- nums = [4, 4, 5], k = 1 -> [5]
"""

class Solution:
    def solveProblemName(self, nums: list[int], k: int) -> int:
        map = dict()
        for num in nums:
            if (num not in map.keys()):
                map[num] = 1
            else:
                map[num] += 1

        new_nums = []
        for key, value in map.items():
            if (value <= k):
                for i in range(value):
                    new_nums.append(key)

        return new_nums
    

if __name__ == "__main__":
    import unittest
    from test_solution import TestExercise

    unittest.main()
