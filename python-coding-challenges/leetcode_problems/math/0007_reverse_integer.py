"""
Problem: 0007. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Description:
Given an integer `x`, reverse its digits. Return 0 if the result overflows a 32-bit signed integer (range: [-2^31, 2^31-1]).

Approach:
1. Math approach – extract digits and build the reversed number, checking for overflow.
2. String approach – convert to string, reverse, and restore sign.

Time Complexity:
- Time: O(n) where n is the number of digits
- Space: O(1)
"""
import numpy as np

class Solution:
    def reverse_string_method(self, x: int) -> int:
        """
        String-based approach to reverse integer.
        """
        s = str(abs(x))[::-1]
        numb = int(s) * (-1 if x < 0 else 1)
        if numb < -2**31 or numb > 2**31 - 1:
            return 0
        return numb

    def reverse_math_method(self, x: int) -> int:
        """
        Math-based approach to reverse integer using numpy for digit placement.
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        arr = []
        while x // 10 != 0:
            current = x % 10
            arr.append(current)
            x = x // 10
        arr.append(x)
        reversed_num = int(np.dot(arr, 10 ** np.arange(len(arr)-1, -1, -1))) * sign
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

    def reverse_math_no_numpy(self, x: int) -> int:
        """
        Math-based approach to reverse integer without numpy, with overflow check.
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            d = x % 10
            x //= 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and d > 7):
                return 0
            rev = rev * 10 + d
        rev *= sign
        return rev if INT_MIN <= rev <= INT_MAX else 0

if __name__ == "__main__":
    sol = Solution()
    # Example 1: Negative number
    print(sol.reverse_math_no_numpy(-12345))  # Expected: -54321
    # Example 2: Positive number
    print(sol.reverse_string_method(120))     # Expected: 21
    # Example 3: Overflow case
    print(sol.reverse_math_method(1534236469)) # Expected: 0