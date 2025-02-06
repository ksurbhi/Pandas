import pandas as pd
# Method 1
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['description'] !='boring') & (cinema['id']%2 ==1)]
    return df.sort_values(by='rating',ascending = False)

# Method 2

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(~cinema['description'].str.contains('boring'))& (cinema['id']%2 != 0)].sort_values('rating', ascending = False)
    
