import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simple function to convert column names in a dataframe
    to lowercase and replace spaces in column names with underscores
    
    Thanks to - https://gist.githubusercontent.com/BexTuychiev/8d9f7af98a8b1102258ae9c7074d8611
    """
    
    new_column_names = [
        column.strip().replace(' ', '_').lower() for column in df.columns
    ]
    
    # Rename column names
    df.columns = new_column_names
    
    return df
