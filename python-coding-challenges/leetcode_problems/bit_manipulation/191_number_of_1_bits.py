"""
        Problem:
            191. Number of 1 Bits
            https://leetcode.com/problems/number-of-1-bits/

        Description:
            Given a positive integer n, return the number of '1' bits in its
            binary representation (Hamming weight).

        Approach:
            Use bitwise operations to check each bit of n:
            - n & 1 checks if the least significant bit is set.
            - n >>= 1 shifts bits right to process the next bit.
            Repeat until n becomes 0.
            This avoids converting n to a string and works in constant space.

        Time Complexity: O(k), where k is the number of bits in n
        Space Complexity: O(1)
        """

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    def hammingWeight(self, n: int) -> int:

        count = 0
        for bit in bin(n)[2:]:
            if bit == '1':
                count += 1
        return count


# Examples
print(Solution().hammingWeight(11))  # Expected output: 3 (1011)
print(Solution().hammingWeight(8))   # Expected output: 1  (1000)
print(Solution().hammingWeight(7))   # Expected output: 3  (111)
