# Informe de salida

## Resumen Ejecutivo

Este informe presenta los resultados del proyecto de Machine Learning diseñado para predecir enfermedades cardíacas. Se detalla cómo los objetivos se lograron mediante el uso de técnicas avanzadas, destacando las contribuciones significativas, desafíos enfrentados y aprendizajes obtenidos durante su desarrollo.

## Resultados del proyecto

### Resumen de los entregables y logros alcanzados  
El principal objetivo del proyecto fue desarrollar un modelo eficiente para predecir la probabilidad de enfermedades cardíacas. Durante el proceso, se lograron los siguientes hitos:  

1. **Preprocesamiento de datos:** Limpieza exhaustiva y estandarización de los datos para garantizar su calidad y relevancia.  
2. **Evaluación de múltiples modelos:** Pruebas realizadas con diversos modelos, incluyendo regresión logística y redes neuronales, para identificar la mejor solución según las métricas de desempeño.  
3. **Selección del mejor modelo:** La regresión logística destacó como la opción más balanceada entre simplicidad, interpretabilidad y rendimiento.  
4. **Implementación y despliegue:** Despliegue exitoso del modelo mediante MLFlow, asegurando trazabilidad y facilidad de mantenimiento. 

### Evaluación del modelo final y comparación con el modelo base  
El modelo final basado en regresión logística demostró un rendimiento sólido en las métricas seleccionadas:  

- **Accuracy:** 0.95, lo que indica un alto nivel de predicciones correctas en general.  
- **F1 Score (macro):** 0.66, reflejando un desempeño balanceado en las distintas clases del problema.
    
Estas métricas resaltan la capacidad del modelo para ofrecer resultados consistentes y confiables. Comparado con otros algoritmos evaluados, la regresión logística destacó no solo por su simplicidad e interpretabilidad, sino también por ofrecer resultados consistentes y robustos.  

### Descripción de los resultados y su relevancia para el negocio  
El modelo desarrollado tiene un impacto significativo en el ámbito médico:  

1. **Diagnóstico Temprano:** La alta precisión del modelo permite identificar a pacientes con mayor probabilidad de padecer enfermedades cardíacas, facilitando diagnósticos tempranos y decisiones clínicas oportunas.
2. **Optimización de Recursos:** Priorización eficiente de tratamientos según factores de riesgo clave.
3. **Apoyo en el tratamiento:** Al identificar rápidamente los factores de riesgo más relevantes, el modelo puede ayudar a personalizar intervenciones y tratamientos, mejorando la calidad de vida de los pacientes.  
4. **Contribución a la salud pública:** Este proyecto aborda uno de los principales desafíos en la medicina moderna, las enfermedades cardíacas, que representan una de las principales causas de mortalidad en los Estados Unidos.
5. **Adaptabilidad del Modelo:** Posibilidad de ser reutilizado en distintos contextos médicos y demográficos.

En resumen, este proyecto no solo optimiza el uso de recursos clínicos, sino que también tiene el potencial de salvar vidas al mejorar significativamente el diagnóstico y manejo de enfermedades cardíacas.  

## Lecciones aprendidas

### Retos Encontrados  
Durante el desarrollo del proyecto, se presentaron varios desafíos que requirieron ajustes en el enfoque y la planificación:  

1. **Integración de múltiples bases de datos:** Inicialmente, contamos con tres fuentes de datos distintas. Fue necesario realizar un análisis exhaustivo para evaluar la viabilidad de su integración, considerando la compatibilidad de las variables y la calidad de los datos. Finalmente, se decidió trabajar con una única base de datos debido a problemas de consistencia y completitud en las otras dos.  
2. **Demanda computacional de modelos complejos:** Al probar modelos más robustos, como redes neuronales, enfrentamos largos tiempos de ejecución y un alto consumo de recursos computacionales, lo que limitó su uso práctico dentro del marco del proyecto.  

### Aprendizajes Clave  
1. **Evaluación con Métricas Balanceadas:** Una de las lecciones más importantes fue no depender únicamente del accuracy como métrica de evaluación, especialmente en escenarios de datos desbalanceados. Incorporar métricas como el F1 score permitió una evaluación más equilibrada del modelo y ayudó a priorizar tanto la precisión como el recall.  
2. **Simplicidad sobre complejidad:** Aunque exploramos varios modelos complejos, el desempeño consistente de la regresión logística destacó la importancia de evaluar la relación costo-beneficio de cada algoritmo. Modelos más simples pueden ofrecer resultados competitivos con menos recursos computacionales y mayor interpretabilidad.  
3. **Calidad de los datos:** La limpieza y selección cuidadosa de la base de datos inicial fue un paso crítico para garantizar la solidez del modelo. Este aprendizaje refuerza la necesidad de dedicar tiempo suficiente a la preparación de datos antes de entrar en la etapa de modelamiento.  

### Recomendaciones para futuros proyectos  
1. **Evaluar la calidad y consistencia de los datos desde el principio:** Antes de integrar múltiples fuentes, realizar un análisis detallado de las variables y la calidad de los datos puede ahorrar tiempo y esfuerzo en etapas posteriores.  
2. **Probar modelos simples primero:** En lugar de priorizar algoritmos complejos, es recomendable comenzar con modelos más sencillos y ajustarlos progresivamente. Esto facilita la comparación inicial y reduce los costos computacionales.  
3. **Incluir métricas adecuadas para el problema:** En proyectos con datos desbalanceados, se deben elegir métricas que reflejen el desempeño real del modelo en todas las clases, como el F1 score o el AUC-ROC, para tomar decisiones más informadas.  
4. **Optimizar los recursos computacionales:** Para proyectos que requieren modelos más complejos, considerar el uso de técnicas como la reducción de dimensionalidad, muestreo eficiente o acceso a infraestructura en la nube puede ser clave para superar limitaciones de hardware.  

Estas lecciones y recomendaciones no solo mejoraron los resultados de este proyecto, sino que también establecen una base sólida para enfrentar retos futuros en el ámbito del aprendizaje automático.  

## Impacto del proyecto

1. **Impacto Médico:** Mejora la capacidad de detección temprana, permitiendo decisiones clínicas más informadas.
2. **Perspectivas Futuras:** Este modelo puede ampliarse con más datos clínicos para incrementar su robustez y utilidad.
3. **Impacto en la Industria:** Este modelo representa una solución innovadora que puede integrarse en plataformas de salud para agilizar diagnósticos y personalizar tratamientos.

## Conclusiones

- El proyecto cumplió con sus objetivos principales, destacándose por su impacto positivo en la predicción y manejo de enfermedades cardíacas.
- Las herramientas utilizadas demostraron ser efectivas y accesibles, estableciendo una base sólida para futuros proyectos.
- Los aprendizajes adquiridos ofrecen valiosas guías para enfrentar retos en el campo del Machine Learning aplicado a la salud.

## Agradecimientos

- Agradecimientos a los Docentes por su guia tecnica y apoyo durante las fases del proyecto 
- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
