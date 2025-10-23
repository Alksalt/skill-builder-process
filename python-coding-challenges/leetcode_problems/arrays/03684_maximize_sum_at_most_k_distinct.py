
from typing import List
"""
        3684. Maximize Sum of At Most K Distinct Elements
        https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

        Problem:
        You are given a positive integer array nums and an integer k.
        Choose at most k elements such that:
          - chosen numbers are DISTINCT
          - their sum is maximized
        Return the chosen numbers in strictly descending order.

        Approach (summary stub):
        - Deduplicate nums, sort descending, return first k.

        Complexity:
        Time: O(n log n) due to sorting.
        Space: O(n) for the set/list.
        """

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        new_nums = list(set(nums))
        new_nums.sort(reverse=True)
        if len(new_nums) >= k:
            return new_nums[:k]
        return new_nums


if __name__ == "__main__":
    # Setup & quick sanity calls (prints current return value of your method)
    sol = Solution()

    # Example 1
    nums1, k1 = [1, 2, 3, 2], 2
    print(sol.maxKDistinct(nums1, k1))  # expected 5 (3 + 2)

    # Example 2
    nums2, k2 = [5, 5, 5], 1
    print(sol.maxKDistinct(nums2, k2))  # expected 5

    # Example 3
    nums3, k3 = [-1, -2, -3, 4], 2
    print(sol.maxKDistinct(nums3, k3))  # expected 4 + (-1) = 3

    # Example 4
    nums3, k3 = [84, 93, 100, 77, 90], 3
    print(sol.maxKDistinct(nums3, k3))  # Output: [100,93,90]