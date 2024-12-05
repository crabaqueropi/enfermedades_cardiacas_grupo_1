import pandas as pd
from pymongo import MongoClient

def connect_to_mongo(connection_str, db_name, collection_name):
    """
    Conecta a MongoDB y retorna una colección.
    """
    try:
        client = MongoClient(connection_str)
        db = client[db_name]
        collection = db[collection_name]
        return collection
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")
        return None

def fetch_data_from_mongo(collection):
    """
    Recupera documentos de MongoDB y retorna un DataFrame.
    """
    try:
        data = list(collection.find())
        if data:
            return pd.DataFrame(data)
        else:
            print("No se encontraron datos.")
            return pd.DataFrame()
    except Exception as e:
        print(f"Error al recuperar datos: {e}")
        return pd.DataFrame()
