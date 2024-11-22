# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Modelo de aprendizaje automático para predecir la probabilidad de una enfermedad cardíaca.

## Objetivo del Proyecto

Se busca implementar un modelo de aprendizaje automático que pueda predecir la probabilidad de que un paciente tenga una enfermedad cardíaca basándose en ciertos factores de riesgo y características médicas. Este modelo se desarrollará utilizando técnicas de machine learning sobre un conjunto de datos que incluya información relevante sobre pacientes, como edad, género, presión arterial, nivel de colesterol, entre otras.

El beneficio de este proyecto se enmarca en el sector de la medicina, ya que las enfermedades cardíacas son una de las principales causas de muerte en los EE. UU. Pacientes con enfermedades cardíacas: El proyecto busca mejorar la detección temprana, el diagnóstico y el tratamiento de las enfermedades cardíacas, lo que a su vez puede mejorar la calidad de vida y la esperanza de vida de los pacientes. 

## Alcance del Proyecto

### Incluye:

#### **1. Descripción de los datos disponibles**  
El conjunto de datos proviene del Sistema de Vigilancia de Factores de Riesgo del Comportamiento (BRFSS) de los CDC, con información recolectada a través de encuestas telefónicas anuales en los 50 estados de EE. UU., el Distrito de Columbia y tres territorios de EE. UU.  
- **Tamaño del conjunto de datos:** Aproximadamente 400,000 registros al año, reducido para este proyecto a un subconjunto más manejable.  
- **Variables originales:** Cerca de 300, de las cuales se seleccionaron 40 para este análisis.  
- **Características clave:** Incluye factores médicos y demográficos como:  
  - Edad.  
  - Género.  
  - Presión arterial.  
  - Nivel de colesterol.  
  - Antecedentes de enfermedades cardíacas.  
  - Información adicional sobre salud general y conductas relacionadas.  
- **Variable objetivo:** `HadHeartAttack`, binaria, con valores:  
  - "Sí" (indicando que el encuestado tiene una enfermedad cardíaca).  
  - "No" (indicando que no tiene ninguna enfermedad cardíaca).  
- **Fuente de los datos:** Kaggle, basado en datos públicos de los CDC, con ajustes para reducir la dimensionalidad y mejorar la aplicabilidad al problema de predicción.  

#### **2. Descripción de los resultados esperados**  
El proyecto busca desarrollar un modelo de aprendizaje automático para predecir la probabilidad de que un paciente sufra de una enfermedad cardíaca, con base en los factores médicos disponibles.  
- **Resultados específicos esperados:**  
  - **Modelo predictivo:** Un clasificador entrenado y validado capaz de categorizar a los pacientes en riesgo de enfermedad cardíaca con alta precisión y sensibilidad.  
  - **Interpretabilidad:** Identificación de los factores de riesgo más influyentes en la predicción, lo que ayudará a los profesionales de la salud a tomar decisiones informadas.  
  - **Métricas de desempeño:** Evaluación del modelo en términos de precisión, sensibilidad, especificidad, y el accuracy.  
  - **Visualizaciones:** Gráficos y reportes que expliquen los hallazgos del modelo y su utilidad en escenarios clínicos.  

#### **3. Criterios de éxito del proyecto**  
El éxito del proyecto será evaluado con base en los siguientes aspectos:  
1. **Desempeño del modelo:**  
   - Lograr un accuracy superior a 0.85, indicando una buena capacidad para distinguir entre pacientes con y sin enfermedades cardíacas.  
   - Sensibilidad y especificidad superiores al 80%, especialmente priorizando la sensibilidad para minimizar falsos negativos.  
2. **Usabilidad del modelo:**  
   - El modelo debe ser interpretable y fácil de usar por profesionales de la salud no técnicos.  
   - Identificación de los principales factores de riesgo, proporcionando información valiosa y accionable para el diagnóstico y tratamiento.  
3. **Impacto clínico:**  
   - Validación del modelo en un conjunto de datos independiente, confirmando su aplicabilidad en entornos reales.  
   - Generación de reportes que faciliten la integración del modelo como una herramienta de apoyo al diagnóstico en la práctica médica.  
4. **Documentación y reproducibilidad:**  
   - Entrega de documentación completa que detalle los pasos del proyecto, desde la limpieza de datos hasta la implementación del modelo.  
   - Garantizar que el proceso sea reproducible y extensible para futuros desarrollos o investigaciones.  


### Excluye:

#### **Descripción de lo que no está incluido en el proyecto**  

El proyecto se limita a predecir la probabilidad de enfermedad cardíaca en base a factores médicos específicos presentes en el conjunto de datos. Sin embargo, hay ciertos aspectos y elementos que no se incluirán:  

1. **Factores externos no médicos:**  
   - **Estilo de vida:** Información sobre la dieta, hábitos de ejercicio, consumo de alcohol o tabaco no será considerada, a menos que ya esté incluida en las variables seleccionadas del conjunto de datos.  
   - **Condiciones laborales:** Factores como niveles de estrés relacionados con el trabajo no serán parte del análisis.  

2. **Predicción de enfermedades cardíacas raras o específicas:**  
   - El modelo se centrará exclusivamente en enfermedades cardíacas comunes que estén reflejadas en la variable objetivo (`HadHeartAttack`) del conjunto de datos. No se extenderá a otras enfermedades cardiovasculares raras o condiciones más complejas.  

3. **Datos demográficos no relevantes:**  
   - Variables como ingresos económicos, nivel educativo, región geográfica específica o información étnica no serán parte del análisis, salvo que estén directamente relacionadas con los factores médicos presentes en los datos.  

4. **Recomendaciones de tratamiento:**  
   - El proyecto no proporcionará recomendaciones personalizadas de tratamiento ni sugerencias de intervención médica para los pacientes. El modelo es únicamente una herramienta de apoyo al diagnóstico.  

5. **Consideraciones éticas y regulatorias:**  
   - La validación ética y regulatoria del uso del modelo en entornos clínicos reales queda fuera del alcance de este proyecto. Su implementación final dependerá de futuras revisiones por parte de las instituciones médicas y reguladoras pertinentes.  

6. **Actualización o mantenimiento del modelo:**  
   - El proyecto no contempla un sistema continuo de actualización del modelo con nuevos datos a futuro ni su implementación en un entorno de producción automatizado.  

7. **Validación externa y uso en otros países:**  
   - El modelo está diseñado y validado específicamente para los datos proporcionados, que corresponden al contexto de los EE. UU. No se garantizará su aplicabilidad en otros países o poblaciones distintas sin ajustes adicionales.  

## Metodología

### **Metodología del proyecto: CRISP-DM**  

Para llevar a cabo este proyecto, utilizaremos la metodología **CRISP-DM (Cross Industry Standard Process for Data Mining)**, ampliamente aceptada para el desarrollo de proyectos de análisis de datos y aprendizaje automático. Este enfoque estructurado nos permitirá abordar el problema de manera eficiente, asegurando claridad y resultados confiables en cada etapa. A continuación, se describen las fases de CRISP-DM aplicadas al proyecto:  

1. **Entendimiento del negocio:**  
   - Definir los objetivos del proyecto: predecir la probabilidad de una enfermedad cardíaca para apoyar la detección temprana y el diagnóstico.  
   - Identificar las necesidades de los beneficiarios, como pacientes y profesionales de la salud, y delimitar los factores médicos relevantes.  
   - Establecer criterios de éxito, como la precisión y sensibilidad del modelo.  

2. **Entendimiento de los datos:**  
   - Analizar las características del conjunto de datos proveniente del Sistema de Vigilancia de Factores de Riesgo del Comportamiento (BRFSS).  
   - Comprender las variables disponibles, incluyendo la variable objetivo (`HadHeartAttack`), y evaluar su relevancia y calidad.  

3. **Preparación de los datos:**  
   - Realizar limpieza de datos, manejo de valores faltantes y codificación de variables categóricas.  
   - Seleccionar y transformar variables relevantes, incluyendo normalización o estandarización según sea necesario.  
   - Dividir el conjunto de datos en subconjuntos de entrenamiento, validación y prueba.  

4. **Modelado:**  
   - Seleccionar algoritmos de aprendizaje automático adecuados, como regresión logística, árboles de decisión, SVM o bosque aleatorio.  
   - Ajustar hiperparámetros para optimizar el desempeño del modelo.  
   - Evaluar el modelo usando métricas como AUC-ROC, sensibilidad, especificidad y precisión.  

5. **Evaluación:**  
   - Validar los resultados del modelo en el conjunto de prueba.  
   - Verificar que el modelo cumpla con los objetivos del proyecto, como identificar correctamente a pacientes en riesgo de enfermedad cardíaca.  
   - Generar reportes con los principales hallazgos y la importancia de las variables predictivas.  

6. **Despliegue:**  
   - Proponer cómo se podría integrar el modelo como una herramienta de apoyo en entornos clínicos.  
   - Documentar todo el proceso, asegurando que el modelo sea reproducible y comprensible para los beneficiarios.  

Esta metodología nos permitirá desarrollar un modelo de aprendizaje automático robusto y efectivo, alineado con las necesidades del sector médico y los objetivos del proyecto.  

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 18 de noviembre al 24 de noviembre de 2024 |
| Preprocesamiento, análisis exploratorio | 1 semanas | del 25 de noviembre al 1 de diciembre de 2024 |
| Modelamiento y extracción de características | 1 semanas | del 2 de diciembre al 8 de diciembre de 2024 |
| Despliegue | 1 semanas | del 9 de diciembre al 15 de diciembre de 2024 |
| Evaluación y entrega final | 1 semanas | del 16 de diciembre al 22 de diciembre de 2024 |

## Equipo del Proyecto

1. Rosmer Manuel Vargas Contreras - CC 1092015057
2. Edwin Alejandro Mateus Rodriguez - CC 1032507993
3. Cristian Adolfo Baquero Pico - CC 1032499677

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
