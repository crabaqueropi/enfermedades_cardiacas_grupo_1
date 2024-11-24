import subprocess
import sys

# Instalar dependencias necesarias
def install_packages():
    """
    Instala todas las dependencias necesarias usando pip.
    """
    required_packages = [
        "dask[complete]", "dask-ml", "scikit-learn", "xarray", 
        "h5py", "pymongo[srv]", "matplotlib", "seaborn"
    ]
    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
    print("Todas las dependencias han sido instaladas.")

install_packages()

# Importar librerías necesarias
import dask.dataframe as dd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient

# Configuración inicial de gráficos
plt.style.use('ggplot')
sns.set_theme()

# Función para leer el token de MongoDB desde una ruta local
def read_mongo_token(token_path):
    """
    Lee el token necesario para conectarse a MongoDB desde un archivo.

    Args:
        token_path (str): Ruta del archivo que contiene el token.
    
    Returns:
        str: Token de conexión.
    """
    try:
        with open(token_path, "r") as f:
            token = f.read().strip().strip('"')
        print("Token leído exitosamente.")
        return token
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {token_path}.")
        return None

# Función para conectar con MongoDB
def connect_to_mongo(connection_str, db_name, collection_name):
    """
    Establece conexión con MongoDB y selecciona una colección.

    Args:
        connection_str (str): Cadena de conexión de MongoDB.
        db_name (str): Nombre de la base de datos.
        collection_name (str): Nombre de la colección.

    Returns:
        Collection: Colección seleccionada de MongoDB.
    """
    try:
        client = MongoClient(connection_str)
        db = client[db_name]
        collection = db[collection_name]
        print(f"Conexión exitosa a MongoDB. Base de datos: {db_name}, Colección: {collection_name}.")
        return collection
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")
        return None

# Función para obtener datos de una colección MongoDB
def fetch_data_from_mongo(collection):
    """
    Recupera todos los documentos de una colección de MongoDB y los convierte en un DataFrame.

    Args:
        collection (Collection): Colección de MongoDB.

    Returns:
        pd.DataFrame: DataFrame con los datos obtenidos.
    """
    try:
        cursor = collection.find()
        data = list(cursor)  # Convertir a lista
        if data:
            df = pd.DataFrame(data)
            print(f"Datos recuperados exitosamente. Total de documentos: {len(df)}.")
            return df
        else:
            print("No se encontraron datos en la colección.")
            return pd.DataFrame()
    except Exception as e:
        print(f"Error al recuperar datos: {e}")
        return pd.DataFrame()

# Análisis exploratorio de datos
def explore_data(df):
    """
    Realiza un análisis exploratorio básico en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame a analizar.
    """
    print("Información del DataFrame:")
    print(df.info())
    print("\nEstadísticas descriptivas:")
    print(df.describe(include='all'))
    print("\nPrimeros 5 registros:")
    print(df.head())

# Visualización básica
def visualize_data(df, numerical_cols):
    """
    Genera gráficos básicos para las columnas numéricas.

    Args:
        df (pd.DataFrame): DataFrame a visualizar.
        numerical_cols (list): Lista de columnas numéricas.
    """
    for col in numerical_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribución de {col}")
        plt.show()

if __name__ == "__main__":
    # Ruta local del archivo con el token
    token_path = r"C:\Users\Ronald\Desktop\enfermedades_cardiacas_grupo_1\token_mongo.txt"
    
    # Leer el token de MongoDB
    token = read_mongo_token(token_path)
    
    if token:
        # Conectar a MongoDB
        collection = connect_to_mongo(token, db_name="mlds3", collection_name="heart_attack")
        
        if collection:
            # Obtener datos de MongoDB
            data_df = fetch_data_from_mongo(collection)
            
            if not data_df.empty:
                # Análisis exploratorio
                explore_data(data_df)

                # Selección de columnas numéricas para visualización
                numerical_columns = data_df.select_dtypes(include=np.number).columns.tolist()
                visualize_data(data_df, numerical_columns)
