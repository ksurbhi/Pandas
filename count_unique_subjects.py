import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate subject-teacher pairs and count unique subjects per teacher
    df = (
        teacher
        .drop_duplicates(['teacher_id', 'subject_id'])  # Remove duplicate subject-teacher pairs
        .groupby('teacher_id')  # Group by teacher
        .size()  # Count unique subjects
        .reset_index(name='cnt')  # Convert to DataFrame and rename column
    )
    return df
