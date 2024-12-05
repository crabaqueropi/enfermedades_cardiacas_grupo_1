from data_acquisition import connect_to_mongo, fetch_data_from_mongo
from data_cleaning import clean_data
import os

# Ruta del token para MongoDB
token_path = "C:/Users/Ka1pa/Desktop/enfermedades_cardiacas_grupo_1-master/scripts/preprocessing/token_mongo.txt"

# Crear carpeta para guardar datos limpios si no existe
os.makedirs("data", exist_ok=True)

def main():
    # Leer el token
    try:
        with open(token_path, "r") as f:
            token = f.read().strip().strip('"')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo del token en {token_path}.")
        return

    # Conectar a MongoDB
    collection = connect_to_mongo(token, db_name="mlds3", collection_name="heart_attack")

    if collection:
        # Adquirir datos
        raw_data = fetch_data_from_mongo(collection)

        if not raw_data.empty:
            # Limpiar datos
            clean_data_df = clean_data(raw_data)

            # Guardar datos limpios
            clean_data_df.to_csv("data/clean_data.csv", index=False)
            print("Datos limpios guardados en 'data/clean_data.csv'.")

if __name__ == "__main__":
    main()
