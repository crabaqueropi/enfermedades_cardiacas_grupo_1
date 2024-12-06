# Definición de los datos

## Origen de los datos

- Los datos provienen de la base de datos pública disponible en [Kaggle: Personal Key Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease).
- Estos datos han sido descargados y almacenados en Google Drive para facilitar su acceso y uso colaborativo.

## Especificación de los scripts para la carga de datos

- Los scripts utilizados para la carga de datos se encuentran en la carpeta `scripts` del proyecto.


### Rutas de origen de datos

- **Ubicación de los archivos de origen:**  
  Los datos se encuentran almacenados en Google Drive y se pueden acceder directamente a través de un enlace compartido o mediante el sistema de control de datos **DVC (Data Version Control)**.
 
  - Nombre del archivo: `heart_2020_cleaned.csv`

- **Estructura de los archivos de origen:**  
  - Formato: CSV delimitado por comas (`,`).
  - Número de filas: 319,795  
  - Número de columnas: 18  

- **Acceso con DVC:**  
  - DVC está configurado para rastrear la versión de los datos. Los datos pueden descargarse mediante:
    ```bash
    dvc pull
    ```

- **Procedimientos de transformación y limpieza de los datos:**  
  - Eliminación de filas duplicadas.
  - Estandarización de etiquetas en variables categóricas.
  - Conversión de tipos de datos según sea necesario.
