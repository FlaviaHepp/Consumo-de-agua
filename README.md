# Análisis del uso del agua en Michigan (2013–2022)

Proyecto de **análisis exploratorio de datos (EDA)** enfocado en el uso del agua en el estado de Michigan, Estados Unidos, entre 2013 y 2022.  
El objetivo principal es analizar patrones de consumo por **industria, fuente de agua, año y condado**, utilizando Python y librerías de análisis de datos.

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

📌 Principales aprendizajes

Aplicación práctica de EDA en un dataset real

Uso combinado de Python + SQL para análisis de datos

Creación de visualizaciones claras para comunicar resultados

Trabajo con datos públicos y estructurados por múltiples dimensiones

🚀 Próximos pasos / mejoras futuras

Normalizar el consumo de agua por población

Incorporar variables climáticas o económicas

Crear un dashboard interactivo (Power BI / Tableau / Streamlit)

Modularizar el código en funciones reutilizables

👤 Autor

Flavia Hepp
Data Analyst Junior
