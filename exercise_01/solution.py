# exercise_01/solution.py

"""
Keep at most k occurrences in a sorted array.


Problem:
You are given a sorted integer array nums and an integer k.
Return an array such that each distinct element appears at most k times,
while preserving the relative order of the elements in nums.


Examples:
- nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 1, 2, 2, 3]
- nums = [1, 2, 3], k = 1 -> [1, 2, 3]
"""

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        print(f"nums = {nums}")
        results = []
        count = 0
        cur = 0

        for idx, num in enumerate(nums):
            if cur != num:
                if cur != 0:
                    print(f"count = {count:>3}")

                cur = num
                count = 1
                print(f"index = {idx:>3} | value = {num:>3} | ", end='')
                results.append(cur)
            else:
                count += 1
                if count <= k:
                    results.append(cur)

        print(f"count = {count:>3}")
        return results