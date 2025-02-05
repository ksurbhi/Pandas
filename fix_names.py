import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Method 1
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    # return users.sort_values(by='user_id')

    #Method 2
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id')
