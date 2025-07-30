import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_excel('Padron_Instituciones.xlsx')
#print(df)

#Ver cuantas filas y columnas tiene el df

num_filas, num_columnas = df.shape
print("Número de filas:", num_filas)
print("Número de columnas:", num_columnas)

#Obtener información detallada del df
print(df.info())

# Imprimir Valores Nulos
valores_nulos = df.isnull()
print(valores_nulos)

# Mostrar Valores Duplicados de las columnas 'Nombre', 'Apellidos'
filas_duplicadas = df[df.duplicated(subset=['Nombre', 'Apellidos'], keep=False)]
print(filas_duplicadas)

#Mostrar Valores Nulos por Columna

num_nulos_por_columna = df.isnull().sum()
print("Número de valores nulos por columna:")
print(num_nulos_por_columna)


#Mostrar Valores Nulos del Dataframe
total_nulos = df.isnull().sum().sum()
print("Número total de valores nulos en el DataFrame:")
print(total_nulos)

# Eliminar filas con valores nulos
df.dropna(inplace=True)
#print(df)

# Rellenar valores nulos con la media de la columna CANTAULAS
df['CANTAULAS'].fillna(df['CANTAULAS'].mean(), inplace=True)
#print(df)

# Rellenar valores nulos con la media de la columna CANTDOC
df['CANTDOC'].fillna(df['CANTDOC'].mean(), inplace=True)
#print(df)


# Rellenar valores nulos con la media de la columna CANTALUM
df['CANTALUM'].fillna(df['CANTALUM'].mean(), inplace=True)
#print(df)

# Encontrar elementos duplicados
duplicados = df[df.duplicated(keep=False)]
print(duplicados)


# Contar la cantidad de elementos duplicados
cantidad_duplicados = len(duplicados)
print(f"Total de elementos duplicados: {cantidad_duplicados}")

#Eliminar Elementos Duplicados

df_sin_duplicados = df.drop_duplicates(subset='ITEM', keep=False)
elementos_duplicados_eliminados = df_sin_duplicados.duplicated().sum()
print(df_sin_duplicados)
print("Número de elementos duplicados eliminados:", elementos_duplicados_eliminados)

#Cambiar tipo de datos de las columnas CANTALUM, CANTDOC, CANTAULAS

df['CANTALUM'] = df['CANTALUM'].astype(int)
df['CANTDOC'] = df['CANTDOC'].astype(int)
df['CANTAULAS'] = df['CANTAULAS'].astype(int)
df['ITEM'] = df['ITEM'].astype(int)
df['UBIGEO'] = df['UBIGEO'].astype(int)
df['CODMOD'] = df['CODMOD'].astype(int)


print(df)

# Mostrar Solo las columnas DEPARTAMENTO y GESTDEP

nuevo_df = df[['DEPARTAMENTO', 'GESTDEP']]
print(nuevo_df)

#Mostrar solo los datos que tengan más de 15 aulas
df_filtrado = df[df['CANTAULAS'] > 15]
print(df_filtrado)

# Ordenar el DataFrame por una columna específica en orden ascendente
df_ordenado = df.sort_values(by='CANTALUM')
print(df_ordenado)

# Ordenar el DataFrame por una columna específica en orden descendente
df_ordenado_desc = df.sort_values(by='CANTALUM', ascending=False)
print(df_ordenado_desc)

# Resumen de estadísticas descriptivas
resumen_estadisticas = df.describe()
print(resumen_estadisticas)

#Visualización de valores faltantes

sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()

# Análisis de correlación de los datos numéricos
df = df.select_dtypes(include=['number'])
correlacion = df.corr()
print(correlacion)



# Gráfico de bigote de la columna 'CANTAULAS'
#sns.boxplot(x=df['CANTAULAS'])
#plt.xlabel('CANTAULAS')
#plt.show()


# Gráfico de bigote de la columna 'CANTALUM'
#sns.boxplot(x=df['CANTALUM'])
#plt.xlabel('CANTALUM')
#plt.show()


# Gráfico de bigote de la columna 'CANTDOC'
#sns.boxplot(x=df['CANTDOC'])
#plt.xlabel('CANTDOC')
#plt.show()

# Filtra el DataFrame para eliminar los valores atípicos
#df = df[(df['CANTAULAS'] >= Bi) & (df['CANTAULAS'] <= Bs)]

#print("Q1:", Q1)
#print("Q3:", Q3)
#print("IQR:", IQR)
#print("Mediana:", Mediana)
#print("Valor mínimo:", Valor_mínimo)
#print("Valor máximo:", Valor_máximo)
#print("Bi (Bigote inferior):", Bi)
#print("Bs (Bigote superior):", Bs)