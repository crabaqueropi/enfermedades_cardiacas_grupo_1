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
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
