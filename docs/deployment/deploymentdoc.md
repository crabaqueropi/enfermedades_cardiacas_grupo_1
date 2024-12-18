# Despliegue de modelos

## Infraestructura

- **Nombre del experimento:** Logistic_Regression_Experiment y Random_Forest_Experiment
- **Nombre del modelo:** logistic_regression_model y random_forest_model
- **Plataforma de despliegue:** El modelo se desplegó en MLFlow en un entorno gratuito de Google Colaboratory
- **Requisitos técnicos:**

  
**Especificaciones técnicas:** El proyecto fue ejecutado en un entorno gratuito de Google Collaboratory y las especificaciones técnicas de estos entornos son:
1. **CPU:**
Procesador Intel Xeon (4 nucleos).
2. **RAM:**
Hasta 12 GB de memoria RAM (sujeto a disponibilidad y carga del sistema).
3. **Disco temporal:**
Almacenamiento temporal de hasta 100 GB.


**Versión de Python**

Python 3.10.12


**Librerías necesarias:**

1. dvc_gdrive version 3.0.1
2. pyngrok version 7.2.2
3. tree version 2.0.2-1
4. mlflow version 2.19.0
5. git version 2.34.1
6. requests version 2.32.3
7. sklearn-pandas version 2.2.0
8. pandas version 2.2.2

- **Requisitos de seguridad:** No aplica
  
- **Diagrama de arquitectura:**

  ![POST](https://github.com/user-attachments/assets/3ea2f9ee-f608-4bdd-9a8c-f50f3bf73684)


## Código de despliegue

- **Archivo principal:** Training_MLFlow.ipynb
- **Rutas de acceso a los archivos:** scripts/training/Training_MLFlow.ipynb
- **Variables de entorno:**

1. os.environ["DRIVEID"]: drive_id para dvc
2. os.environ["GDRIVE_CREDENTIALS_DATA"]: credenciales para dvc
3. os.environ["NGROK_TOKEN"]: token de Ngrok


## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
  ### Requisitos Previos

  1. Crear un entorno virtual:

     python -m venv venv
     source venv/bin/activate  # Windows: .\venv\Scripts\activate
  
  2. Instalar las dependencias necesarias:

     pip install mlflow joblib dvc_gdrive pyngrok pandas sklearn-pandas requests

  3. Configurar las variables de entorno:
     import os
     os.environ["DRIVEID"] = "<drive_id_para_dvc>"
     os.environ["GDRIVE_CREDENTIALS_DATA"] = "<contenido_de_credentials.json>"
     os.environ["NGROK_TOKEN"] = "<tu_ngrok_token>"
     
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
  ### Exportación del Modelo
  Guardar el modelo entrenado en un archivo que permita su despliegue:

    import joblib
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    joblib.dump(model, "model.pkl")

- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
  ### Despliegue Local con MLFlow
  Usar MLFlow para servir el modelo:

      mlflow models serve -m "path/to/model" --port 5000

  Probar la API REST:

      curl -X POST -H "Content-Type: application/json" \
           -d '{"data": [[1, 2, 3]]}' http://127.0.0.1:5000/invocations

  ### Exposición del Servicio con Ngrok
  Instalar Ngrok:

      pip install pyngrok

  Configurar tu token de Ngrok:

      ngrok config add-authtoken <tu_ngrok_token>

  Iniciar un túnel hacia el puerto del servidor:

      ngrok http 5000

  Usar la URL generada por Ngrok para acceder al modelo desde cualquier ubicación.
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
  ### Actualización del Modelo
  1. Exportar un nuevo modelo entrenado.
  2. Reemplazar el archivo del modelo en el directorio de despliegue.
  3. Reiniciar el servidor MLFlow:
      mlflow models serve -m "path/to/updated_model" --port 5000
  ### Monitoreo
  Usar los registros de MLFlow para revisar solicitudes y errores:
      mlflow ui
