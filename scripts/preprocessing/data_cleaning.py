import pandas as pd
import numpy as np

def clean_data(df):
    """
    Limpieza básica de datos.
    """
    df = df.copy()
    # Eliminar columnas innecesarias
    if '_id' in df.columns:
        df = df.drop(columns=['_id'])
    
    # Manejo de valores faltantes
    for col in df.select_dtypes(include=[np.number]):
        df[col] = df[col].fillna(df[col].mean())  # Llenar numéricos con la media
    for col in df.select_dtypes(include=[object]):
        df[col] = df[col].fillna('Desconocido')  # Llenar strings con 'Desconocido'
    
    # Eliminar duplicados
    df = df.drop_duplicates()

    return df
