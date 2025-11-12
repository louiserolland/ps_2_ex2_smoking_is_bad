# file: utils.py
from pathlib import Path
import pandas as pd


def load_smoking_data(filename: str = "smoking_data.csv") -> pd.DataFrame:
    """
    Load the smoking dataset from the 'data' folder.

    Parameters
    ----------
    filename : str
        The name of the CSV file (default is 'smoking_data.csv').

    Returns
    -------
    pd.DataFrame
        The loaded data as a pandas DataFrame.
    """
    data_path = Path("data") / filename
    if not data_path.exists():
        raise FileNotFoundError(f"❌ Could not find {data_path.resolve()}")
    return pd.read_csv(data_path)
