# %%
# Problem: 3668. Restore Finishing Order
# Link: https://leetcode.com/problems/restore-finishing-order/
# Difficulty: Easy

from typing import List



class Solution:
    def restoreFinishingOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        result = []
        for i in order:
            if i in friends:
                result.append(i)
        return result


# %%
# Quick runnable examples
def run_examples():
    sol = Solution()

    # Example 1
    order1 = [3, 1, 2, 5, 4]
    friends1 = [1, 3, 4]
    print("Ex1:", sol.restoreFinishingOrder(order1, friends1))  # Expected [3, 1, 4]

    # Example 2
    order2 = [1, 4, 5, 3, 2]
    friends2 = [2, 5]
    print("Ex2:", sol.restoreFinishingOrder(order2, friends2))  # Expected [5, 2]

    # Example 3: edge case with only one friend
    order3 = [2, 3, 1]
    friends3 = [1]
    print("Ex3:", sol.restoreFinishingOrder(order3, friends3))  # Expected [1]


if __name__ == "__main__":
    run_examples()