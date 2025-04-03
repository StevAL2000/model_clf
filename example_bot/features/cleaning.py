import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a DataFrame by efficiently handling NaN values in numeric columns.

    Args:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Use vectorization to fill NaN values in numeric columns with 0
    numeric_cols = df.select_dtypes(include=['number']).columns
    if not numeric_cols.empty:
        df.loc[:, numeric_cols] = df[numeric_cols].fillna(0)

    # Use vectorization to fill NaN values in non-numeric columns with an empty string
    other_cols = df.select_dtypes(exclude=['number']).columns
    if not other_cols.empty:
        df.loc[:, other_cols] = df[other_cols].fillna('')

    # Infer data types
    df = df.infer_objects(copy=False)
    return df


if __name__ == "__main__":
    # Testing
    data = {
        'dates': [pd.Timestamp('2023-01-01'), pd.Timestamp('2023-01-02'), pd.Timestamp('2023-01-03')],
        'numbers': [1, None, 3],
        'strings': ['example', 'example2', 'example3'],
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    cleaned_df = clean_dataframe(df)

    print("\nCleaned DataFrame:")
    print(cleaned_df)