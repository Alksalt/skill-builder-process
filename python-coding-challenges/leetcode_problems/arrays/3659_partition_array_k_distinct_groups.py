# %%
# Problem: 3659. Partition Array Into K-Distinct Groups
# Link: https://leetcode.com/problems/partition-array-into-k-distinct-groups/
# Difficulty: Medium

from typing import List



class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        pass



# %%
# Runnable examples
def run_examples():
    sol = Solution()

    # Ex 1: feasible simple case
    nums1 = [1, 2, 3, 1, 2, 3]
    k1 = 3
    print("Ex1:", sol.partitionArray(nums1, k1))  # Expected: True

    # Ex 2: infeasible due to duplicates > group capacity
    nums2 = [5, 5, 5, 1, 2, 3]
    nums4 = [1,2,3,4,5,6,7,8,8]
    k2 = 3
    print("Ex2:", sol.partitionArray(nums2, k2))  # Expected: False

    # Ex 3: edge-ish; k=2, balanced pairs with distinct-in-group requirement
    nums3 = [7, 7, 8, 8]
    k3 = 2
    print("Ex3:", sol.partitionArray(nums3, k3))  # Expected: True


if __name__ == "__main__":
    run_examples()