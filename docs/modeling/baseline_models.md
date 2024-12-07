# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. En este caso, se ha utilizado una regresión logística para predecir la probabilidad de una enfermedad cardíaca basándose en un conjunto de datos preprocesados.

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo:

Edad

Sexo

IMC (Índice de Masa Corporal)

Estado Fumador

Diabetes

Colesterol Total

Presión Arterial

Frecuencia Cardiaca

Historia Familiar de Enfermedades Cardíacas

Estas variables fueron seleccionadas por su relevancia clínica y su potencial predictivo basado en el análisis exploratorio de datos.

## Variable objetivo

La variable objetivo utilizada en el modelo es:

Diagnóstico de Enfermedad Cardíaca: Indicador binario donde 1 representa la presencia de la enfermedad y 0 su ausencia.

## Evaluación del modelo

## Métricas de evaluación

Las siguientes métricas fueron utilizadas para evaluar el rendimiento del modelo baseline:

Precisión (Accuracy): Porcentaje de predicciones correctas.

Sensibilidad (Recall): Capacidad del modelo para identificar casos positivos.

Especificidad: Capacidad del modelo para identificar casos negativos.

AUC-ROC: Área bajo la curva ROC, que mide la capacidad del modelo para distinguir entre clases.

## Resultados de evaluación

Métrica

Valor

Precisión

0.78

Sensibilidad

0.85

Especificidad

0.72

AUC-ROC

0.81

Los resultados muestran un desempeño inicial prometedor para el modelo baseline, con un balance razonable entre sensibilidad y especificidad.

## Análisis de los resultados

El modelo baseline presenta fortalezas y debilidades:

Fortalezas:

Sensibilidad alta, lo que significa que identifica correctamente la mayoría de los casos positivos.

AUC-ROC por encima de 0.8, indicando una buena capacidad de discriminación.

Debilidades:

Especificidad baja, lo que puede llevar a un mayor número de falsos positivos.

No incluye técnicas avanzadas de selección de características ni optimización de hiperparámetros.

## Conclusiones

El modelo baseline proporciona una buena línea de partida para evaluar futuros modelos. Aunque su desempeño es aceptable, existe margen para mejorar mediante:

Ingeniería de características.

Optimización de hiperparámetros.

Implementación de modelos más complejos, como árboles de decisión o redes neuronales.

Estas mejoras pueden aumentar la especificidad y la precisión general del modelo.

## Referencias

Documentación interna del proyecto.

"Introduction to Statistical Learning" - Gareth James et al.

Notebooks de análisis exploratorio y scripts de modelado disponibles en el repositorio del proyecto.
