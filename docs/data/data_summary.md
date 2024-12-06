# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos (EDA) realizado al conjunto de datos disponible en la carpeta `eda`.

---

## Resumen general de los datos

A continuación, se describen las características principales del conjunto de datos:

- **Número total de observaciones:** 319,795
- **Número total de variables:** 18
- **Tipo de variables:** 
  - Numéricas: 4 (`BMI`, `PhysicalHealth`, `MentalHealth`, `SleepTime`)
  - Categóricas: 14
- **Presencia de valores faltantes:** Ninguna variable tiene valores faltantes.
- **Tamaño en memoria:** 43.9 MB

### Estadísticas descriptivas de las variables numéricas:

| Variable          | Media    | Desviación estándar | Mínimo  | 25%    | Mediana | 75%    | Máximo |
|-------------------|----------|---------------------|---------|--------|---------|--------|--------|
| BMI               | 28.33    | 6.36                | 12.02   | 24.03  | 27.34   | 31.42  | 94.85  |
| PhysicalHealth    | 3.37     | 7.95                | 0.00    | 0.00   | 0.00    | 2.00   | 30.00  |
| MentalHealth      | 3.90     | 7.95                | 0.00    | 0.00   | 0.00    | 3.00   | 30.00  |
| SleepTime         | 7.10     | 1.44                | 1.00    | 6.00   | 7.00    | 8.00   | 24.00  |

---

## Resumen de calidad de los datos

### Valores faltantes
No hay valores faltantes en las variables.

### Valores extremos
- Variables como `BMI` tienen valores extremos en su rango máximo (94.85), pero no se identificaron errores evidentes.

### Duplicados
- Se encontraron **18,078 filas duplicadas**, lo que representa aproximadamente el **5.65%** del total de observaciones.
- Acciones tomadas: Las filas duplicadas fueron eliminadas en el script del EDA.

---

## Variable objetivo

La variable objetivo del análisis es `HeartDisease`, que indica si un participante tiene o no enfermedad cardíaca. Es una variable categórica con los valores:

- `Yes` (Presencia de enfermedad cardíaca)
- `No` (Ausencia de enfermedad cardíaca)

### Distribución de la variable objetivo:

| Categoría | Conteo   | Porcentaje (%) |
|-----------|----------|----------------|
| No        | 292,422  | 91.44%         |
| Yes       | 27,373   | 8.56%          |

### Observaciones:
- La variable objetivo está altamente desbalanceada, con una proporción significativamente mayor de participantes sin enfermedad cardíaca.

### Gráficos:
- Un gráfico de barras fue generado para visualizar esta distribución en el script de la carpeta `eda`.

---

## Variables individuales

A continuación, se presentan los puntos clave del análisis de las variables:

### Variables numéricas
1. **BMI (Índice de Masa Corporal):**
   - Rango: 12.02 a 94.85
   - Mediana: 27.34
   - Distribución: Sesgada hacia la derecha debido a los valores extremos.

2. **PhysicalHealth (Días de mala salud física):**
   - La mayoría de los valores son 0, lo que indica que muchos participantes reportaron no tener días de mala salud física.

3. **MentalHealth (Días de mala salud mental):**
   - Similar a `PhysicalHealth`, la mayoría de los valores son 0, pero los valores mayores tienen mayor dispersión.

4. **SleepTime (Horas promedio de sueño):**
   - La mayoría de los participantes duermen entre 6 y 8 horas por noche.

### Variables categóricas
1. **Smoking y AlcoholDrinking:**
   - `Smoking`: Variables binaria (`Yes`, `No`), con una mayor proporción de no fumadores.
   - `AlcoholDrinking`: Menos participantes reportaron consumo de alcohol.

2. **Sex y AgeCategory:**
   - `Sex`: Mayor proporción de mujeres en comparación con hombres.
   - `AgeCategory`: Predominan las edades entre 55 y 59 años.

3. **Race y GenHealth:**
   - `Race`: La categoría predominante es `White`.
   - `GenHealth`: La mayoría de los participantes calificaron su salud como "Good" o "Very good".

Gráficos de barras y histogramas para estas variables fueron generados en el script del EDA.

---



## Relación entre variables explicativas y variable objetivo

### Matriz de correlación:
- Se generó una matriz de correlación para las variables numéricas.
- La variable `PhysicalHealth` mostró una correlación positiva moderada con `HeartDisease`.

### Gráficos:
- Gráficos de dispersión y diagramas de barras fueron utilizados para analizar las relaciones entre las variables más importantes y `HeartDisease`.

---

## Conclusiones

1. **Calidad de los datos:**
   - Los datos son de buena calidad, sin valores faltantes. Sin embargo, se identificaron duplicados que fueron eliminados en el script del EDA.

2. **Desbalance de la variable objetivo:**
   - La variable `HeartDisease` está desbalanceada, lo que requiere atención especial al entrenar modelos predictivos.

3. **Variables clave:**
   - Variables como `BMI`, `PhysicalHealth`, y `SleepTime` son altamente predictivas para la variable objetivo.

Para más información, consulta el script en la carpeta `eda`.

