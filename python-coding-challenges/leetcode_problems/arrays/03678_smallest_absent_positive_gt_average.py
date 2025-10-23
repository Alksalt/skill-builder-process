# 03678_smallest_absent_positive_gt_average.py
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        unique = set(nums)
        i = int(avg) + 1
        while True:
            if i > 0 and i not in unique:
                return i
            i += 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1 (from prompt)
    nums1 = [3, 5]
    print(sol.smallestAbsent(nums1))  # expected 6

    # Example 2 (duplicates and gaps)
    nums2 = [1, 2, 2, 4]
    # avg = 9/4 = 2.25; smallest missing positive > 2.25 is 3
    print(sol.smallestAbsent(nums2))  # expected 3

    # Example 3 (includes negatives and large values)
    nums3 = [-2, -1, 1, 100]
    # avg = 98/4 = 24.5; smallest missing positive > 24.5 is 25 (if 25 not in nums)
    print(sol.smallestAbsent(nums3))  # expected 25