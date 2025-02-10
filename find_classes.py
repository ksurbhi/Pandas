import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of each class
    df = courses.groupby('class').size().reset_index(name='cnt')

    # Filter classes with at least 5 students and return only 'class' column
    return df[df['cnt']>=5][['class']]
    
