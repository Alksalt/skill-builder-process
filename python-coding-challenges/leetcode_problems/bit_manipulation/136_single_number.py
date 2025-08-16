"""
   Problem:
       136. Single Number
       https://leetcode.com/problems/single-number/

   Description:
       Given a non-empty array of integers, every element appears twice except for one.
       Find that single one.
       Must run in linear time and use only constant extra space.

   Approach:
       Use bitwise XOR to cancel out duplicate numbers.
       XORing all elements leaves only the single number.

   Time Complexity: O(n)
   Space Complexity: O(1)
       """
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# Examples
print(Solution().singleNumber([2, 2, 1]))        # Expected output: 1
print(Solution().singleNumber([4, 1, 2, 1, 2]))  # Expected output: 4
print(Solution().singleNumber([1]))              # Expected output: 1
