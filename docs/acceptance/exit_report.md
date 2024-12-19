# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

### Resumen de los entregables y logros alcanzados  
El proyecto tuvo como objetivo principal desarrollar un modelo de aprendizaje automático capaz de predecir la probabilidad de que un paciente tenga una enfermedad cardíaca. Durante el desarrollo, se lograron importantes hitos:  

1. **Preprocesamiento de datos:** Se realizó una limpieza y transformación exhaustiva del conjunto de datos, asegurando que los factores de riesgo y características médicas relevantes estuvieran correctamente representados.  
2. **Evaluación de múltiples modelos:** Se probaron varios algoritmos, incluyendo regresión logística, árboles de decisión, redes neuronales y métodos de detección de anomalías.  
3. **Selección del mejor modelo:** A través de un riguroso análisis de métricas, se eligió la regresión logística como el modelo más adecuado, optimizado para maximizar el balance entre precisión y sensibilidad.  
4. **Implementación y despliegue:** El modelo final fue integrado y desplegado para su consumo utilizando **MLflow**, garantizando la trazabilidad y facilidad de mantenimiento en futuras iteraciones.  

### Evaluación del modelo final y comparación con el modelo base  
El modelo final basado en regresión logística demostró un rendimiento sólido en las métricas seleccionadas:  

- **Accuracy:** 0.95, lo que indica un alto nivel de predicciones correctas en general.  
- **F1 Score (macro):** 0.66, reflejando un desempeño balanceado en las distintas clases del problema.  

Comparado con otros algoritmos evaluados, la regresión logística destacó no solo por su simplicidad e interpretabilidad, sino también por ofrecer resultados consistentes y robustos, superando a modelos más complejos en términos de generalización y facilidad de implementación.  

### Descripción de los resultados y su relevancia para el negocio  
El modelo desarrollado tiene un impacto significativo en el ámbito médico:  

1. **Mejora en la detección temprana:** La alta precisión del modelo permite identificar a pacientes con mayor probabilidad de padecer enfermedades cardíacas, facilitando diagnósticos tempranos y decisiones clínicas oportunas.  
2. **Apoyo en el tratamiento:** Al identificar rápidamente los factores de riesgo más relevantes, el modelo puede ayudar a personalizar intervenciones y tratamientos, mejorando la calidad de vida de los pacientes.  
3. **Contribución a la salud pública:** Este proyecto aborda uno de los principales desafíos en la medicina moderna, las enfermedades cardíacas, que representan una de las principales causas de mortalidad en los Estados Unidos.  

En resumen, este proyecto no solo optimiza el uso de recursos clínicos, sino que también tiene el potencial de salvar vidas al mejorar significativamente el diagnóstico y manejo de enfermedades cardíacas.  

## Lecciones aprendidas

### Principales desafíos y obstáculos encontrados  
Durante el desarrollo del proyecto, se presentaron varios desafíos que requirieron ajustes en el enfoque y la planificación:  

1. **Integración de múltiples bases de datos:** Inicialmente, contamos con tres fuentes de datos distintas. Fue necesario realizar un análisis exhaustivo para evaluar la viabilidad de su integración, considerando la compatibilidad de las variables y la calidad de los datos. Finalmente, se decidió trabajar con una única base de datos debido a problemas de consistencia y completitud en las otras dos.  
2. **Demanda computacional de modelos complejos:** Al probar modelos más robustos, como redes neuronales, enfrentamos largos tiempos de ejecución y un alto consumo de recursos computacionales, lo que limitó su uso práctico dentro del marco del proyecto.  

### Lecciones aprendidas  
1. **Importancia de las métricas adecuadas:** Una de las lecciones más importantes fue no depender únicamente del accuracy como métrica de evaluación, especialmente en escenarios de datos desbalanceados. Incorporar métricas como el F1 score permitió una evaluación más equilibrada del modelo y ayudó a priorizar tanto la precisión como el recall.  
2. **Simplicidad sobre complejidad:** Aunque exploramos varios modelos complejos, el desempeño consistente de la regresión logística destacó la importancia de evaluar la relación costo-beneficio de cada algoritmo. Modelos más simples pueden ofrecer resultados competitivos con menos recursos computacionales y mayor interpretabilidad.  
3. **Calidad de los datos:** La limpieza y selección cuidadosa de la base de datos inicial fue un paso crítico para garantizar la solidez del modelo. Este aprendizaje refuerza la necesidad de dedicar tiempo suficiente a la preparación de datos antes de entrar en la etapa de modelamiento.  

### Recomendaciones para futuros proyectos  
1. **Evaluar la calidad y consistencia de los datos desde el principio:** Antes de integrar múltiples fuentes, realizar un análisis detallado de las variables y la calidad de los datos puede ahorrar tiempo y esfuerzo en etapas posteriores.  
2. **Probar modelos simples primero:** En lugar de priorizar algoritmos complejos, es recomendable comenzar con modelos más sencillos y ajustarlos progresivamente. Esto facilita la comparación inicial y reduce los costos computacionales.  
3. **Incluir métricas adecuadas para el problema:** En proyectos con datos desbalanceados, se deben elegir métricas que reflejen el desempeño real del modelo en todas las clases, como el F1 score o el AUC-ROC, para tomar decisiones más informadas.  
4. **Optimizar los recursos computacionales:** Para proyectos que requieren modelos más complejos, considerar el uso de técnicas como la reducción de dimensionalidad, muestreo eficiente o acceso a infraestructura en la nube puede ser clave para superar limitaciones de hardware.  

Estas lecciones y recomendaciones no solo mejoraron los resultados de este proyecto, sino que también establecen una base sólida para enfrentar retos futuros en el ámbito del aprendizaje automático.  

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
