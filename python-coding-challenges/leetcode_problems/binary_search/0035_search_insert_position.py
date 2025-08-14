"""
Problem: 34. Find First and Last Position of Element in Sorted Array
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Description:
Given an array of integers `nums` sorted in non-decreasing order and a target value `target`,
return the starting and ending position of `target` in `nums`.
If `target` is not found in the array, return [-1, -1].

Approach:
1. Use two separate binary searches:
   - First binary search finds the leftmost (first) index of `target`.
   - Second binary search finds the rightmost (last) index of `target`.
2. Both searches use the "record and bias" technique:
   - When `nums[mid] == target`, record `mid` and keep searching to the left (for first) or right (for last).
3. If the first search returns -1, `target` is not present, return [-1, -1].

Time Complexity:
- Time: O(log n) — two binary searches.
- Space: O(1) — only a few variables for bounds and answers.
"""
import timeit
class Solution:
    def first(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                if nums[middle] == target:
                    ans = middle
                right = middle - 1
            else:
                left = middle + 1
        return ans
    def last(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                if nums[middle] == target:
                    ans = middle
                left = middle + 1
            else:
                right = middle - 1
        return ans
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        first = self.first(nums, target)
        if first != -1:
            return [first, self.last(nums, target)]
        else:
            return [-1, -1]


    def searchRange2(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        n = len(nums)
        left = 0
        right = n - 1
        result = []

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                result.append(middle)
                result.append(middle)
                left = middle
                right = middle
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if not result:
            return [-1, -1]
            
        while (right + 1 < n) and (nums[right + 1] == target):
            right += 1
        result[1] = right
        
        while (left - 1 >= 0) and  nums[left - 1] == target:
            left -= 1
        result[0] = left

        return result


if __name__ == "__main__":
    sol = Solution()

    big_nums = list(range(10_000_000))  # 0 .. 9,999,999

    # Example 1: Target present in the middle
    print(sol.searchRange(big_nums, 5_000_000),
          timeit.timeit(lambda: sol.searchRange(big_nums, 5_000_000), number=10))  # Expected: [5000000, 5000000]

    # Example 2: Target not present
    print(sol.searchRange(big_nums, 10_000_001),
          timeit.timeit(lambda: sol.searchRange(big_nums, 10_000_001), number=10))  # Expected: [-1, -1]

    # Example 3: Target at the end
    print(sol.searchRange(big_nums, 9_999_999),
          timeit.timeit(lambda: sol.searchRange(big_nums, 9_999_999), number=10))  # Expected: [9999999, 9999999]
    print(sol.searchRange2(big_nums, 10_000_001),
          timeit.timeit(lambda: sol.searchRange2(big_nums, 10_000_001), number=10))
    big_nums = [8] * 5_000_000
    target = 8
    print(
        "Expand-outward:",
        timeit.timeit(lambda: sol.searchRange2(big_nums, target), number=1)
    )

    # True binary version (O(log n))
    print(
        "Binary search:",
        timeit.timeit(lambda: sol.searchRange(big_nums, target), number=1))