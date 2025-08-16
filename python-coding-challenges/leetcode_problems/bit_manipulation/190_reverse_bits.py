"""
    Problem:
        190. Reverse Bits
        https://leetcode.com/problems/reverse-bits/

    Description:
        Reverse the bits of a given 32-bit unsigned integer.
        The result should be an unsigned integer representing
        the reversed bit order.

    Approach:
        Initialize result = 0.
        Loop exactly 32 times:
            - Shift result left by 1 to make space.
            - Add the least significant bit of n (n & 1) to result.
            - Shift n right by 1 to move to the next bit.
        Return result.

    Time Complexity: O(1)  (32 iterations regardless of n)
    Space Complexity: O(1)
        """
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result += n & 1
            n >>= 1
        return result

# Examples
print(Solution().reverseBits(43261596))  # Expected output: 964176192
print(Solution().reverseBits(0b00000010100101000001111010011100))  # Expected: 964176192
print(Solution().reverseBits(0b11111111111111111111111111111101))  # Expected: 3221225471
