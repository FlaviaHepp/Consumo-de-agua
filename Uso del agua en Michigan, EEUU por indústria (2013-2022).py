"""
Uso del agua en Michigan por industria, fuente y año (2013-2022)

Este conjunto de datos proporciona información detallada sobre el uso del agua en diversas industrias de Michigan desde 2013 hasta 2022, categorizada 
por fuente de agua. Los datos se compilan a partir de fuentes públicas en Michigan.gov.

Características principales:

Industria: Variable categórica que indica el sector industrial asociado a los datos de uso de agua (por ejemplo, Comercial-Institucional, 
Industrial-Manufactura, Irrigación, etc.).

Año: Variable numérica que representa el año en el que se registraron los datos de uso de agua.

Grandes Lagos (galones): Esta columna representa la cantidad de agua extraída de los Grandes Lagos por una industria específica en un año determinado. Las unidades se expresan en galones.

Agua subterránea (galones): esta columna representa la cantidad de agua extraída de fuentes subterráneas por una industria específica en un año 
determinado. Las unidades se expresan en galones.

Aguas superficiales continentales (galones): esta columna representa la cantidad de agua extraída de fuentes de aguas superficiales continentales 
(por ejemplo, ríos, arroyos) por una industria específica en un año determinado. Las unidades se expresan en galones.

Galones totales: esta columna representa el consumo total de agua de cada industria en un año determinado, calculado como la suma del agua extraída 
de los Grandes Lagos, las aguas subterráneas y las fuentes de agua superficial continental. Las unidades se expresan en galones.

Usos potenciales:
Analizar las tendencias de uso de agua en diferentes industrias en Michigan a lo largo del tiempo, categorizadas por fuente de agua.
Identificar industrias con alta dependencia de fuentes de agua específicas y explorar posibles estrategias de conservación.
Comparar los patrones de extracción de agua de diferentes fuentes (Grandes Lagos, aguas subterráneas, aguas superficiales continentales) en todas las 
industrias.
Investigar las correlaciones entre los patrones de uso del agua y factores como la actividad económica o la densidad de población (si se fusionan 
datos adicionales).
Diccionario de datos:

Notas de limpieza de datos:
Las tablas disponibles públicamente para cada año y industria se fusionaron en las columnas de índice: condado, año e industria.
Se eliminaron todas las filas (10) con valores NaN.
"""


import os
import pandas as pd #
from matplotlib import pyplot as plt 
plt.style.use('dark_background')
import seaborn as sns # gráficos y visualizaciones avanzadas 
from sklearn.preprocessing import LabelEncoder # codificar variables categóricas
import matplotlib.ticker as ticker
#Consultas SQL
from pandasql import sqldf # Funcionalidad SQL de Pandas


data_path = 'water_use_data_2013_to_2022.csv'
df = pd.read_csv(data_path, index_col=0)
print(df.head())

# Establecer nombre de índice
df.rename_axis('index', inplace=True)
print(df.info())

print(df.head())

ordered_list = ['Total All Sectors', 
                'Electric Power Generation',
                'Public Water Supply',
                'Industrial-Manufacturing',
                'Irrigation',
                'Livestock',
                'Commercial-Institutional',
                'Other'
                ]

fig = plt.figure(figsize=(15,15))

sns.barplot(x="industry", y="total_gallons_all_sources", order=ordered_list, data=df)

plt.xticks(rotation=80, ha='right')
plt.xlabel('Tipo de industria\n')
plt.ylabel('Total de agua pública utilizada (gal)\n')
plt.title('Total de agua pública utilizada por la industria en Michigan (2013-2022)\n', fontsize = '16', fontweight = 'bold')

plt.show()

df['industry'].unique()

# Definir el número de filas y columnas para la cuadrícula de la trama secundaria
rows = 2
cols = 4
fig, axes = plt.subplots(rows, cols, figsize=(12, 8))

# Extraiga tipos de industria únicos
unique_industries = df['industry'].unique()

# Recorre cada subtrama y tipo de industria
for i in range(rows):
    for j in range(cols):
        if i * cols + j >= len(unique_industries):  # Comprobar si se alcanzó el límite
            axes[i, j].axis('off')  # Ocultar subtramas vacías
            continue
    
        # Seleccionar datos para la industria actual
        industry_data = df.loc[df['industry'] == unique_industries[i * cols + j]]
    
        # Cree un diagrama de líneas para el total de galones por año para esta industria
        sns.barplot(x='year', 
                     y='total_gallons_all_sources', 
                     data=industry_data,
                     ax=axes[i, j],
                     color='green'
                    )
        # Establecer el título de la trama secundaria como el nombre de la industria
        axes[i, j].set_title(unique_industries[i * cols + j])
        
        # Recorre cada subtrama y rota los ticks
        for tick in axes[i, j].get_xticklabels():
            tick.set_rotation(45)
            tick.set_ha('right')
        
        # Configuración de etiquetas x e y
        axes[i, j].set_ylabel('Total de agua pública utilizada (gal)')
        axes[i, j].set_xlabel('Año')
            
# Ajustar el diseño y la apariencia
fig.suptitle('Galones totales de todas las fuentes por año por industria\n',
             fontsize=14,
             weight='bold')
plt.tight_layout()  # Ajustar el espacio entre subtramas
plt.show()

# Extraer nombres de columnas de fuentes de agua
water_sources = ['gallons_from_great_lakes', 'gallons_from_inland_surface', 'gallons_from_groundwater']
# Elija colores de pilas
colors = ['fuchsia', 'cyan', 'lime']

# Crear un diagrama de barras apiladas y una leyenda
for color, stack in zip(colors, water_sources):
    ax = sns.barplot(x="year", 
                     y=stack, 
                     data=df, 
                     color=color, 
                     errorbar=None
                     )
    
plt.legend(title='Fuente\n', labels=['Grandes Lagos', 'Superficie interior', 'Agua subterránea'])
plt.xticks(rotation=45, ha='right')  # Girar xticks 45 grados

# Configuración de etiquetas y títulos x e y
plt.ylabel('Total de galones utilizados (apilados por fuente)\n')
plt.xlabel('Año\n')
plt.title('Total de agua utilizada por fuente por año\n', fontsize = '16', fontweight = 'bold')

# Ajustar diseño
plt.tight_layout()
plt.show()

# Definir el número de filas y columnas para la cuadrícula de la trama secundaria
rows = 3
fig, axes = plt.subplots(rows, 1, figsize=(12, 25))

# Extraiga tipos de industria únicos
water_sources = ['gallons_from_great_lakes',
                 'gallons_from_groundwater',
                 'gallons_from_inland_surface']

# Lista de colores de la subtrama
colors = sns.color_palette('tab10', 3)

# Recorre cada subtrama y tipo de industria
for i in range(rows):
    # Cree un diagrama de líneas para el total de galones por año para esta industria
    sns.barplot(x='year', 
                y=water_sources[i], 
                data=df,
                ax=axes[i],
                color=colors[i]
                )
    # Establecer el título de la trama secundaria como el nombre de la industria
    axes[i].set_title(water_sources[i])
        
    # Recorre cada subtrama y rota los ticks
    for tick in axes[i].get_xticklabels():
        tick.set_rotation(0)
        tick.set_ha('center')
        
    # Configuración de etiquetas x e y
    axes[i].set_ylabel('Total de agua pública utilizada (gal)')
    axes[i].set_xlabel('Año')
    axes[i].set_title(water_sources[i].replace('_', ' ').title(), weight='bold')
            
# Ajustar el diseño y la apariencia
fig.suptitle('Variación del agua utilizada por año y fuente\n',
             fontsize=16,
             weight='bold')
plt.tight_layout()  # Ajustar el espacio entre subtramas
plt.subplots_adjust(top=0.93)
plt.show()

# Eliminar columna del condado
df_corr = df.drop('county', axis=1)

# Codificar columna de industria
le = LabelEncoder()
df_corr['industry'] = le.fit_transform(df_corr['industry'])

correlation = df_corr.corr()  # Codificar columna de industria
sns.heatmap(correlation, annot=True, cmap='spring')  # Anotar con valores de correlación
plt.title('Matriz de correlación (etiqueta codificada)\n', fontsize = '16', fontweight = 'bold')
plt.show()


#Consumo total de agua por año:
result1 = sqldf('''
SELECT year, SUM(total_gallons_all_sources)/1000000000 AS total_gallons_Billions
FROM df
GROUP BY year
ORDER BY total_gallons_Billions;
''')
print(result1)

# Valores ordenados
sorted_result1 = result1.sort_values('total_gallons_Billions', ascending=False).year

# diagrama de barras nacido en el mar
sns.barplot(x='year', y='total_gallons_Billions', data=result1, order=sorted_result1)

# Personaliza la figura
plt.xticks(rotation=45, ha='right')
plt.xlabel('Año\n')
plt.ylabel('Total de agua utilizada (miles de millones de galones)\n')
plt.title('Uso de agua por año\n', fontsize = '16', fontweight = 'bold')

# Mostrar trama
plt.show()

#Porcentaje de uso de agua por fuente:
result2 = sqldf('''
SELECT year, 
(SUM(gallons_from_great_lakes)*100) / SUM(total_gallons_all_sources) AS pct_great_lakes,
(SUM(gallons_from_inland_surface)*100) / SUM(total_gallons_all_sources) AS pct_inland_surface,
(SUM(gallons_from_groundwater)*100) / SUM(total_gallons_all_sources) AS pct_groundwater
FROM df
GROUP BY year
ORDER BY year;
''')
print(result2)

# Trama de pandas
result2.plot(kind='bar', x='year')

# Personaliza la figura
plt.xticks(rotation=45, ha='right')
plt.xlabel('Año\n')
plt.ylabel('Total de agua utilizada (millones de galones)\n')
plt.title('Uso de agua por año para cada fuente\n', fontsize = '16', fontweight = 'bold')
plt.legend(['Porcentaje Grandes Lagos', 'Porcentaje de lagos interiores', 'Porcentaje de agua subterránea'])

# Mostrar trama
plt.show()

#Los 3 años principales para el uso del agua:
result3 = sqldf('''
SELECT year, 
SUM(total_gallons_all_sources) / 1000000000 AS total_gallons_all_sources_Billions
FROM df
GROUP BY year
ORDER BY total_gallons_all_sources_Billions DESC
LIMIT 3;
''')
print(result3)

# Trama de pandas
result3.plot(kind='bar', x='year', color='pink')

# Personaliza la figura
plt.xticks(rotation=0, ha='center')
plt.xlabel('Año\n')
plt.ylabel('Total de agua utilizada (miles de millones de galones)\n')
plt.title('Los 3 años principales de uso de agua en Michigan\n', fontsize = '16', fontweight = 'bold')
plt.ylim(7000, 8000)
plt.legend().remove()

# Cree un nuevo objeto de texto con la anotación y colóquelo dentro del cuadro
plt.annotate("*The y-axis does not begin at 0*", xy=(2,7700), xycoords='data',
             bbox=dict(boxstyle="round", fc="none", ec="green", alpha=0.2), ha='center',
             xytext=(-40,60), textcoords='offset points', weight='bold')
# Mostrar trama
plt.show()

#Los 3 años principales en cuanto a uso de agua en el condado de Charlevoix:
result4 = sqldf('''
SELECT county, year, 
SUM(total_gallons_all_sources) / 1000000 AS total_gallons_all_sources_Millions
FROM df
WHERE county = 'Charlevoix'
GROUP BY year
ORDER BY total_gallons_all_sources_Millions DESC
LIMIT 3;
''')
print(result4)

# Trama de pandas
result4.plot(kind='bar', x='year', color='pink')

# Personaliza la figura
plt.xticks(rotation=0, ha='center')
plt.xlabel('Año\n')
plt.ylabel('Total de agua utilizada (millones de galones)\n')
plt.title('Los 3 años principales de uso de agua en el condado de Charlevoix\n', fontsize = '16', fontweight = 'bold')
plt.legend().remove()

# Mostrar trama
plt.show()

#3 años principales de uso del agua de riego en el condado de Charlevoix:
result5 = sqldf('''
SELECT year, 
SUM(total_gallons_all_sources) / 1000000 AS total_gallons_irrigation_Millions
FROM df
WHERE county = 'Charlevoix' 
AND industry = 'Irrigation'
GROUP BY year
ORDER BY total_gallons_irrigation_Millions DESC
LIMIT 3;
''')
print(result5)

# Trama de pandas
result5.plot(kind='bar', x='year', color='brown')

# Personaliza la figura
plt.xticks(rotation=0)
plt.xlabel('Año\n')
plt.ylabel('Total de agua utilizada (millones de galones)\n')
plt.title('Los 3 años principales de uso de agua de riego en el condado de Charlevoix\n', fontsize = '16', fontweight = 'bold')
plt.legend().remove()

# Mostrar trama
plt.show()

#Los 3 principales condados de Michigan por uso de agua en 2022:
result6 = sqldf('''
SELECT county, 
SUM(total_gallons_all_sources) / 1000000000 AS total_gallons_Billions
FROM df
WHERE year = 2022
GROUP BY county
ORDER BY total_gallons_Billions DESC
LIMIT 3;
''')
print(result6)

# Trama de pandas
result6.plot(kind='bar', x='county', color='purple')

# Personaliza la figura
plt.xticks(rotation=45, ha='right')
plt.xlabel('Condado')
plt.ylabel('Total de agua utilizada (miles de millones de galones)\n')
plt.title('Los 3 condados principales por uso de agua en Michigan (2013-2022)\n', fontsize = '16', fontweight = 'bold')
plt.legend().remove()

# Mostrar trama
plt.show()

#Proporciones de fuentes de agua en el condado de Berrien:
result7 = sqldf('''
SELECT county, 
CAST(SUM(gallons_from_great_lakes) * 100 AS FLOAT) / CAST(SUM(total_gallons_all_sources) AS float) AS pct_great_lakes,
CAST(SUM(gallons_from_inland_surface) * 100 AS FLOAT) / CAST(SUM(total_gallons_all_sources) AS FLOAT) AS pct_inland_surface,
CAST(SUM(gallons_from_groundwater) * 100 AS FLOAT) / CAST(SUM(total_gallons_all_sources) AS FLOAT) AS pct_groundwater
FROM df
WHERE county = 'Berrien'
GROUP BY county
''')
print(result7)

# Convierta result7 a formato largo y elimine el índice de fila duplicado
result7 = pd.melt(result7, var_name='pct_source', value_name='Berrien')
result7 = result7.iloc[1:]

# Ordenar valores
sorted_result7 = result7.sort_values('pct_source').Berrien

# Trama de pandas
sorted_result7.plot(kind='bar', x='pct_source')

# Personaliza la figura
plt.xticks(rotation=45, ha='right', ticks=(0,1,2), labels=('Grandes Lagos', 'Superficie interior', 'Agua subterránea'))
plt.xlabel('Fuente de agua\n')
plt.ylabel('Proporción del agua total utilizada (%)\n')
plt.title('Uso de agua por fuente en el condado de Berrien (2013-2022)\n', fontsize = '16', fontweight = 'bold')
plt.legend().remove()

# Mostrar trama
plt.show()

#Uso del agua por parte de la industria en el condado de Berrien:
berrien_industry_df = sqldf('''
WITH RankedIndustries AS (
  SELECT 
    industry,
    total_gallons_all_sources,
    DENSE_RANK() OVER (ORDER BY SUM(total_gallons_all_sources) DESC) AS rank
  FROM df
  WHERE county = 'Berrien'
  GROUP BY industry
)
SELECT 
  industry,
  total_gallons_all_sources / 1000000 AS total_usage_sector_Millions,
  rank
FROM RankedIndustries
WHERE industry != 'Total All Sectors'
ORDER BY rank;
''')
print(berrien_industry_df)

# diagrama de barras nacido en el mar
sns.barplot(x='industry', y='total_usage_sector_Millions', data=berrien_industry_df)

# Personaliza la figura
plt.xticks(rotation=60, ha='right')
plt.xlabel('Industria\n')
plt.ylabel('Total de agua utilizada (millones de galones)\n')
plt.title('Uso de agua por industria en el condado de Berrien\n', fontsize = '16', fontweight = 'bold')

# mostrar la trama
plt.show()


