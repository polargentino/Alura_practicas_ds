# ✅ Código Completo: Exploración de Datos con pandas

'''
🔍 ¿Qué hace este código?
Te da un mapa completo de los datos que tenés: tamaño, nombres de columnas, tipos de datos, valores 
faltantes, y resumen estadístico de las columnas numéricas.

Con esto podés empezar a planear tu análisis, limpieza o visualización.


'''
import pandas as pd

# Cargar datos desde la URL
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
tienda = pd.read_csv(url)

# Ver cantidad de filas y columnas
print("Forma del DataFrame (filas, columnas):")
print(tienda.shape)

# Ver nombres de columnas
print("\nNombre de las columnas:")
print(tienda.columns)

# Ver los primeros 5 registros
print("\nPrimeras 5 filas:")
print(tienda.head())

# Ver los últimos 5 registros
print("\nÚltimas 5 filas:")
print(tienda.tail())

# Ver información general del DataFrame (tipos de datos, nulos, etc.)
print("\nInformación general del DataFrame:")
print(tienda.info())

# Ver estadísticas descriptivas para columnas numéricas
print("\nEstadísticas básicas:")
print(tienda.describe())

# Ver cantidad de valores nulos por columna
print("\nValores nulos por columna:")
print(tienda.isnull().sum())
