"""
    Problem:
        2269. Find the K-Beauty of a Number
        https://leetcode.com/problems/find-the-k-beauty-of-a-number/

    Description:
        The k-beauty of an integer num is defined as the number of substrings of
        length k in its decimal representation that are non-zero and divide num evenly.
        Leading zeros are allowed in substrings. Substrings may overlap.

    Approach:
        - Convert num to string for easy slicing.
        - Use a sliding window of length k to extract each substring.
        - Convert substring to integer; skip if zero to avoid division by zero.
        - If num % substring == 0, increment the count.
        - Return the final count.

    Time Complexity: O(d * k), where d is the number of digits in num
    Space Complexity: O(d) for the string representation
        """
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        new_num = str(num)
        n = len(new_num)
        if n < k:
            return 0
        count = 0
        for i in range(n - k + 1):
            substr = int(new_num[i:i+k])
            if substr != 0 and num % substr == 0:
                count += 1
        return count


# Examples
print(Solution().divisorSubstrings(240, 2))     # Expected output: 2
print(Solution().divisorSubstrings(430043, 2))  # Expected output: 2
