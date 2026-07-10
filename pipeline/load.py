import pandas as pd

def load_raw(path: str) -> pd.DataFrame:
    """
    Load raw stock data from a CSV file.
    Takes in the file path as a string and returns a pandas DataFrame.
    """
    return pd.read_csv(path)