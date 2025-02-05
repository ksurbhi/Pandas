import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if N > len(df) or N <1:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N):[None]})
    else:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N):[df.iloc[N-1]]})
