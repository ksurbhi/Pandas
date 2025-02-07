import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace = True) # sort values so that all the smaller id's comes 1st 
    person.drop_duplicates('email', inplace = True) # then remove duplicate emails
    
