import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='event_date', inplace = True)
    activity.drop_duplicates('player_id', inplace = True)
    return activity[['player_id','event_date']].rename(columns = {'event_date':'first_login'})
