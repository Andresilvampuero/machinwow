"""
This is a boilerplate pipeline 'relleno_datos'
generated using Kedro 0.19.7
"""
import pandas as pd
def fill_missing_values(zones: pd.DataFrame) -> pd.DataFrame:
    
    return zones.fillna({'Subzone': 'None', 'Size': 0, 'Area': 'None', 'Zone': 'None', 'Min_rec_level': 0, 'Max_rec_level': 0, 'Min_bot_level': 0, 'Max_bot_level': 0})