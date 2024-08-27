"""
This is a boilerplate pipeline 'normalizar_datos'
generated using Kedro 0.19.7
"""
import pandas as pd

def strip_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los nombres de las columnas eliminando espacios en blanco al principio y al final."""
    df.columns = df.columns.str.strip()
    return df

def convert_columns_to_int(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte las columnas especificadas a enteros."""
    df['Min_rec_level'] = df['Min_rec_level'].astype(int)
    df['Max_rec_level'] = df['Max_rec_level'].astype(int)
    df['Min_bot_level'] = df['Min_bot_level'].astype(int)
    df['Max_bot_level'] = df['Max_bot_level'].astype(int)
    return df

def process_wowah_data(df: pd.DataFrame) -> pd.DataFrame:
    """Reemplaza valores en la columna 'guild' directamente en el DataFrame original."""
    df["guild"] = df["guild"].replace(-1, 0)
    return df