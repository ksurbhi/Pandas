import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Method 1
    employees['bonus'] = employees.apply(lambda x: x['salary']
    if (x['employee_id'] % 2 ==1) & (~x['name'].startswith('M'))
    else 0, axis = 1)
    return employees[['employee_id','bonus']].sort_values(by='employee_id')

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Method 2
    employees['bonus'] = 0
    cond =(employees['employee_id']%2 ==1) & (~employees['name'].str.startswith('M'))
    employees.loc[cond,'bonus'] = employees['salary']
    return employees[['employee_id','bonus']].sort_values(by='employee_id')
  
