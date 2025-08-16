"""
   Problem:
       2119. A Number After a Double Reversal
       https://leetcode.com/problems/a-number-after-a-double-reversal/

   Description:
       Given an integer num, reverse it to get reversed1, then reverse reversed1
       to get reversed2. Return True if reversed2 equals num, otherwise False.

   Approach:
       - If num is 0, double reversal will still be 0 -> return True.
       - If num ends with a zero (num % 10 == 0), the trailing zero will be lost
         in the first reversal, so double reversal won't match -> return False.
       - Otherwise, double reversal will produce the original number -> return True.

   Time Complexity: O(1)
   Space Complexity: O(1)
       """

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        remainder = num % 10
        if remainder == 0:
            return False
        else:
            return True




# Examples
print(Solution().isSameAfterReversals(526))   # Expected output: True
print(Solution().isSameAfterReversals(1800))  # Expected output: False
print(Solution().isSameAfterReversals(0))     # Expected output: True
