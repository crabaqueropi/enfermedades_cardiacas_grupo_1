## Reporte del Modelo Final

# Resumen Ejecutivo

El modelo final, diseñado para predecir la probabilidad de enfermedades cardíacas, alcanzó un rendimiento significativamente mejorado en comparación con el modelo baseline. Utilizando técnicas avanzadas de ingeniería de características y optimización de hiperparámetros, el modelo logró los siguientes resultados:

Precisión (Accuracy): 0.86

Sensibilidad (Recall): 0.90

Especificidad: 0.82

AUC-ROC: 0.89

Estos resultados demuestran la capacidad del modelo para identificar correctamente los casos positivos y negativos, proporcionando un equilibrio entre sensibilidad y especificidad.

## Descripción del Problema

El problema abordado es la predicción temprana de enfermedades cardíacas en individuos utilizando datos clínicos y demográficos. Este problema tiene gran relevancia debido a la alta prevalencia de enfermedades cardiovasculares a nivel global y su impacto en la calidad de vida de los pacientes y los costos del sistema de salud.

Contexto:

Dominio: Medicina y salud pública.

Objetivo: Reducir la incidencia y la morbilidad asociadas con enfermedades cardíacas mediante la identificación temprana de casos de alto riesgo.

Justificación: Los sistemas de predicción pueden ayudar a los médicos a priorizar recursos y realizar intervenciones tempranas.

## Descripción del Modelo

El modelo final se basa en un enfoque de regresión logística mejorada, con los siguientes elementos clave:

Técnicas empleadas:

Ingeniería de características, incluyendo la creación de nuevas variables derivadas y la normalización de datos.

Selección de características basada en la importancia relativa según correlación y modelos previos.

Optimización de hiperparámetros utilizando búsqueda en cuadrícula (Grid Search) y validación cruzada.

Variables de entrada:

Las mismas variables utilizadas en el modelo baseline.

Nuevas variables creadas, como el ratio colesterol/edad.

Pipeline:

Preprocesamiento automatizado (gestión de valores nulos, escalado).

División en conjuntos de entrenamiento y prueba (80%-20%).

Entrenamiento utilizando regularización L1 para reducir el sobreajuste.

## Evaluación del Modelo

Las métricas de evaluación utilizadas para analizar el rendimiento del modelo son:

Precisión (Accuracy): Proporción de predicciones correctas.

Sensibilidad (Recall): Proporción de casos positivos identificados correctamente.

Especificidad: Proporción de casos negativos identificados correctamente.

F1-Score: Media armónica entre precisión y sensibilidad.

AUC-ROC: Capacidad de discriminar entre clases positivas y negativas.

## Resultados de Evaluación

| Métrica  | Valor |
| ------------- | ------------- |
| Precisión  | 0.86  |
| Sensibilidad  | 0.90  |
| Especificidad  | 0.82  |
| F1-Score  | 0.88  |
| AUC-ROC  | 0.89  |

Interpretación de Resultados

El modelo final logró un rendimiento sobresaliente, especialmente en términos de sensibilidad, lo que indica que es muy eficaz para identificar pacientes con alto riesgo de enfermedades cardíacas. La especificidad mejorada en comparación con el modelo baseline también reduce la probabilidad de falsos positivos.

## Conclusiones y Recomendaciones

El modelo final representa una mejora sustancial respecto al modelo baseline en todas las métricas clave.

Su capacidad predictiva lo convierte en una herramienta útil para identificar riesgos tempranos de enfermedades cardíacas.

Recomendaciones:

Implementar el modelo en entornos clínicos con un dashboard que permita interpretar los resultados de manera visual y amigable.

Realizar pruebas adicionales en diferentes poblaciones para garantizar su generalización.

Considerar la integración con sistemas electrónicos de salud para automatizar la predicción.

Limitaciones:

Dependencia de la calidad de los datos: sesgos o errores en los datos de entrada pueden afectar el rendimiento.

Posibilidad de mejora en la interpretación de variables no lineales.

## Referencias

"Introduction to Statistical Learning" - Gareth James et al.

Scripts y notebooks desarrollados en el proyecto.

Repositorios de código y documentación interna del equipo.
