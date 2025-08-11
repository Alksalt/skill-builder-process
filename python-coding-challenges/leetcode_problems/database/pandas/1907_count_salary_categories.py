"""
Problem: 1907. Count Salary Categories (Pandas)
Link: https://leetcode.com/problems/count-salary-categories/

Description:
    Write a solution to count the number of bank accounts for each salary category:
        - Low Salary: income < 20000
        - Average Salary: 20000 <= income <= 50000
        - High Salary: income > 50000
    The output should include all categories even if the count is zero.

Approach:
    Use `pd.cut` with bins [-inf, 20000, 50000, inf] and corresponding labels
    to classify incomes into categories. Then apply `value_counts(sort=False)`
    to count the occurrences in each category, preserving label order. Finally,
    reset the index and rename columns to match the required output.

Time Complexity: O(N)
Space Complexity: O(N)
"""
import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cats = ['Low Salary', 'Average Salary', 'High Salary']
    df = pd.cut(x=accounts['income'],
            right=False,
            labels=cats, 
            bins=[-np.inf, 20_000, 50_000, np.inf]
            ).value_counts(sort=False).reset_index(name='accounts_count').rename(columns={'income':'category'})
    return df


# -------- Examples --------
# Example 1 (from prompt)
ex1 = pd.DataFrame({
    'account_id': [3, 2, 8, 6],
    'income':     [108939, 12747, 87709, 91796],
})
print(count_salary_categories(ex1))

# Example 2 (edge: all low)
ex2 = pd.DataFrame({
    'account_id': [1, 2, 3],
    'income':     [0, 19999, 15000],
})
print(count_salary_categories(ex2))

# Example 3 (edge: empty input)
ex3 = pd.DataFrame(columns=['account_id', 'income'])
print(count_salary_categories(ex3))
