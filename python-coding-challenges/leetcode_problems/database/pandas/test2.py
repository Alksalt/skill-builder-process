import pandas as pd
import numpy as np

ex1 = pd.DataFrame({
    'account_id': [3, 2, 8, 6],
    'income':     [108939, 12747, 87709, 91796],
})

cats = ['Low Salary', 'Average Salary', 'High Salary']
df = pd.cut(x=ex1['income'],
            labels=cats, 
            bins=[-np.inf, 20_000, 50_000, np.inf]
            ).value_counts(sort=False).reset_index(name='accounts_count').rename(columns={'income':'category'})

print(df)
