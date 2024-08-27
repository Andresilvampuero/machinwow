"""
This is a boilerplate pipeline 'recorte_outliners'
generated using Kedro 0.19.7
"""
import numpy as np
import pandas as pd
from scipy import stats

def filter_outliers(df: pd.DataFrame) -> pd.DataFrame:
    z = np.abs(stats.zscore(df["level"]))
    return df[z < 3]