# Consumo-de-agua
Proyecto: Análisis del Uso del Agua en Michigan (2013-2022)

Realicé un análisis detallado del uso del agua en Michigan, categorizado por industria, fuente de extracción y año, con el objetivo de identificar patrones de consumo, dependencias por sector y oportunidades de conservación de recursos hídricos.
Herramientas: python, pandas, matplotlib, seaborn, pandasql, LabelEncoder.
**Resultados clave:**
Identificación de las industrias y regiones con mayor consumo de agua, proporcionando insights para estrategias de sostenibilidad.
Creación de gráficos interactivos para comunicar visualmente las tendencias y proporciones de uso por fuente (Grandes Lagos, aguas subterráneas, aguas superficiales).
Desarrollo de una matriz de correlación para explorar relaciones entre variables clave.
**Habilidades aplicadas:**
Análisis exploratorio de datos (EDA), visualización avanzada, consultas SQL en Python, limpieza y preprocesamiento de datos.

# Uso del agua en Michigan (2013–2022)
2. Descripción breve

Un párrafo que explique qué analiza el proyecto y con qué objetivo.

Este proyecto analiza el uso del agua en el estado de Michigan entre 2013 y 2022,
desagregado por industria, fuente de agua y condado, utilizando datos públicos.

3. Objetivos

Qué preguntas busca responder el análisis.

## Objetivos
- Analizar la evolución del consumo de agua por industria
- Comparar el uso de distintas fuentes de agua
- Identificar años y condados con mayor consumo

4. Datos

De dónde salen los datos y qué contienen.

## Datos
- Fuente: Michigan.gov (datos públicos)
- Periodo: 2013–2022
- Variables principales:
  - Industria
  - Año
  - Condado
  - Uso de agua por fuente (Grandes Lagos, aguas subterráneas y superficiales)
  - Consumo total

5. Tecnologías / librerías

Qué herramientas se usaron.

## Tecnologías utilizadas
- Python
- pandas
- matplotlib
- seaborn
- scikit-learn
- pandasql

6. Estructura del repositorio

Muy útil para que otros entiendan qué hace cada archivo.

## Estructura del repositorio
├── water_use_data_2013_to_2022.csv
├── Uso del agua en Michigan, EEUU por indústria (2013-2022).py
├── README.md

7. Cómo ejecutar el proyecto

Pasos simples.

## Cómo ejecutar
1. Clonar el repositorio
2. Instalar dependencias:
   pip install pandas matplotlib seaborn scikit-learn pandasql
3. Ejecutar el script:
   python Uso del agua en Michigan, EEUU por indústria (2013-2022).py

8. Resultados / visualizaciones

Qué produce el script.

## Resultados
El proyecto genera:
- Gráficos de barras por industria y año
- Comparación de fuentes de agua
- Rankings de años y condados con mayor consumo
- Análisis de correlación entre variables

9. Posibles mejoras (opcional pero suma mucho)

Muestra pensamiento crítico.

## Mejoras futuras
- Normalizar el consumo por población
- Incorporar datos climáticos
- Crear un dashboard interactivo

# Análisis del uso del agua en Michigan (2013–2022)

Proyecto de **análisis exploratorio de datos (EDA)** enfocado en el uso del agua en el estado de Michigan, Estados Unidos, entre 2013 y 2022.  
El objetivo principal es analizar patrones de consumo por **industria, fuente de agua, año y condado**, utilizando Python y librerías de análisis de datos.

Este proyecto forma parte de mi **portfolio como Data Analyst Junior**.

---

## 📌 Objetivos del proyecto

- Analizar la evolución temporal del uso del agua en Michigan
- Comparar el consumo entre diferentes industrias
- Evaluar la dependencia de distintas fuentes de agua:
  - Grandes Lagos
  - Aguas subterráneas
  - Aguas superficiales continentales
- Identificar:
  - Años con mayor consumo
  - Condados con mayor uso de agua
  - Industrias más intensivas en consumo hídrico

---

## 📊 Datos

- **Fuente:** Datos públicos de Michigan.gov  
- **Periodo:** 2013–2022  
- **Nivel de detalle:** Industria, condado, año y fuente de agua  

### Variables principales
- `industry`: sector industrial
- `county`: condado
- `year`: año
- `gallons_from_great_lakes`
- `gallons_from_groundwater`
- `gallons_from_inland_surface`
- `total_gallons_all_sources`

> Se realizó limpieza de datos eliminando filas con valores nulos y unificación de tablas anuales.

---

## 🛠️ Herramientas y tecnologías

- **Python**
- **pandas** → limpieza y manipulación de datos  
- **matplotlib & seaborn** → visualización  
- **pandasql** → consultas SQL sobre DataFrames  
- **scikit-learn** → codificación de variables categóricas  

---

## 📈 Análisis realizados

- Análisis exploratorio de datos (EDA)
- Gráficos de barras por industria y año
- Comparación del uso de agua por fuente
- Visualizaciones por condado
- Rankings:
  - Años con mayor consumo
  - Condados con mayor uso de agua
- Análisis de correlación entre variables numéricas

---

## 📂 Estructura del repositorio

├── water_use_data_2013_to_2022.csv
├── Uso del agua en Michigan, EEUU por indústria (2013-2022).py
├── README.md


---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar las dependencias:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn pandasql
Ejecutar el script:

python Uso del agua en Michigan, EEUU por indústria (2013-2022).py

## Autor
Flavia Hepp  
Proyecto de análisis de datos
