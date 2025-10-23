# 03683_earliest_time_to_finish_one_task.py
from typing import List

"""
       3683. Earliest Time to Finish One Task
       https://leetcode.com/problems/earliest-time-to-finish-one-task/

       Problem:
       You are given a list of tasks. Each task is represented as [start, duration].
       A task that starts at time `s` and has duration `d` finishes at time `s + d`.
       You can choose exactly one task to execute. Return the earliest possible
       finishing time among all tasks.

       Approach:
       - Iterate through all tasks.
       - For each task, compute finish time = start + duration.
       - Keep track of the minimum finish time seen so far.
       - Return the minimum.

       Complexity:
       Time: O(n), where n = number of tasks (we check each task once).
       Space: O(1), only a constant variable for tracking the best result.
       """
def earliest_time(tasks: List[List[int]]) -> int:
    best = float('inf')
    for start, duration in tasks:
        finish = start + duration
        if finish < best:
            best = finish
    return best



if __name__ == "__main__":
    # Example 1 (contest-style):
    tasks1 = [[1, 6], [2, 3]]
    print(earliest_time(tasks1))   # expected 5 (2 + 3) — you can finish one task at time 5.  [oai_citation:0‡LeetCode](https://leetcode.com/problems/earliest-time-to-finish-one-task/?utm_source=chatgpt.com)

    # Example 2 (edgey mix; from feedback thread):
    tasks2 = [[10, 50], [1, 100], [20, 5], [50, 1], [2, 200], [99, 1], [30, 10]]
    print(earliest_time(tasks2))   # expected 25 (20 + 5).  [oai_citation:1‡GitHub](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/32299?utm_source=chatgpt.com)

    # Example 3 (simple sanity):
    tasks3 = [[5, 1], [1, 10], [3, 2]]
    print(earliest_time(tasks3))   # expected 5 (3 + 2)