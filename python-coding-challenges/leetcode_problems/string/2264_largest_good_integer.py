"""
Problem: 2264. Largest 3-Same-Digit Number in String
Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/

Description:
Given a numeric string `num`, return the largest "good integer" as a string.
A good integer is a substring of length 3 consisting of the same digit repeated three times.
If there are multiple good integers, return the largest one.
If no such substring exists, return an empty string.

Approaches:
1. largestGoodInteger_find:
   - Check digits from '9' down to '0', build a triple (e.g., '777'),
     and use the `in` operator to see if it appears in `num`.
   - This takes advantage of CPython's highly optimized C substring search.
   - Early exit on the first match guarantees the result is the largest possible.
   - Best for typical inputs where large triples are likely.

2. largestGoodInteger:
   - Iterate through `num`, checking each center position `i` for a triple match (`num[i-1] == num[i] == num[i+1]`).
   - Keep track of the largest triple found so far by lexicographical comparison.
   - Simple and clear; runs in O(n) time.

3. largestGoodInteger2:
   - Block-scan version that groups identical digits into runs and skips over entire runs in one step.
   - If a run length is >= 3, it's a valid triple; update `largest_so_far` if the digit is larger.
   - Skips any run that cannot beat the current best, reducing checks.
   - Early exit on "999".
   - Useful for very large inputs or cases with long runs of repeated digits.

Time Complexity:
- largestGoodInteger_find: O(10·n) worst-case, often much faster due to early exit and C-level search.
- largestGoodInteger: O(n)
- largestGoodInteger2: O(n) with fewer iterations in practice due to run-skipping and pruning.

Space Complexity:
- All approaches: O(1) additional space.
"""
class Solution:
    def largestGoodInteger_find(num: str) -> str:
        for d in map(str, range(9, -1, -1)):
            triple = d * 3
            if triple in num:
                return triple
        return ""

    def largestGoodInteger(self, num: str) -> str:
        largest_so_far = ""
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                candidate = num[i - 1:i + 2]
                if candidate > largest_so_far:
                    largest_so_far = candidate
        return largest_so_far
    def largestGoodInteger2(self, num: str) -> str:
        largest_so_far = ""
        i = 0
        n = len(num)
        while i < n:
            if largest_so_far and num[i] <= largest_so_far[0]:
                j = i + 1
                while j < n and num[j] == num[i]:
                    j += 1
                i = j
                continue

            j = i + 1
            while j < n and num[i] == num[j]:
                j += 1
            run_len = j - i
            if run_len >= 3:
                largest_so_far = num[i] * 3
                if largest_so_far == '999':
                    return largest_so_far
            i = j
        return largest_so_far


if __name__ == "__main__":
    sol = Solution()

    # Example 1: Contains "777"
    print(sol.largestGoodInteger("6777133339"))  # Expected: "777"

    # Example 2: Contains "000"
    print(sol.largestGoodInteger("2300019"))  # Expected: "000"

    # Example 3: Multiple good integers, take largest ("999" vs "777")
    print(sol.largestGoodInteger("42352338"))  # Expected: ""

    # Example 4: No triple digits
    print(sol.largestGoodInteger("123456789"))  # Expected: ""