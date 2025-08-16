
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return 1

        count = 0
        while n:
            n >>= 1
            count += 1
        return count


# Examples
print(Solution().countBits(2))  # Expected: [0, 1, 1]
print(Solution().countBits(5))  # Expected: [0, 1, 1, 2, 1, 2]
