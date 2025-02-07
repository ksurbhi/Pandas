import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df_low = accounts[accounts['income']<20000]
    df_avg = accounts[(accounts['income']>=20000) & (accounts['income']<=50000)]
    df_high = accounts[accounts['income']>50000]
    df = pd.DataFrame([['Low Salary',len(df_low)],['Average Salary',len(df_avg)],['High Salary',len(df_high)]], columns = ['category','accounts_count'])
    return df
    # Code is correct but showing time limit exceed
    # accounts['category'] = accounts.apply(lambda x: 'Low Salary'
    # if x['income']<20000 else
    # 'Average Salary' if (20000 <= x['income'])and (x['income'] <= 50000 )else
    # 'High Salary',axis =1  )
    # result = accounts['category'].value_counts().reindex(['Low Salary', 'Average Salary', 'High Salary'], fill_value=0).reset_index(name= 'accounts_count')
    # return result
