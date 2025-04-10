# ✅ Código Completo: Filtrado de Datos con pandas (¡Filtro de Electrodomésticos Arreglado!)

'''
🔍 ¿Qué aprendés con este código?
- Cómo usar condiciones para filtrar filas según valores.
- Cómo combinar múltiples condiciones con & (AND) y | (OR).
- Cómo buscar texto dentro de una columna tipo string (.str.contains()).
- Cómo seleccionar columnas específicas para enfocarte en lo importante.
'''

import pandas as pd
import unicodedata

# Función para normalizar texto (quitar acentos y convertir a minúsculas)
def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower().replace(" ", "_")

# Cargar el archivo con manejo de errores
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
try:
    tienda = pd.read_csv(url)
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Limpiar los nombres de columna: minúsculas, sin espacios ni acentos
tienda.columns = [normalize_text(col.strip()) for col in tienda.columns]

# Ver columnas reales para validar
print("Columnas disponibles:", tienda.columns.tolist())

# Validar que las columnas necesarias existen
required_columns = ['precio', 'categoria_del_producto', 'producto']
missing_columns = [col for col in required_columns if col not in tienda.columns]
if missing_columns:
    print(f"Error: Faltan las siguientes columnas necesarias en el DataFrame: {missing_columns}")
    exit()
else:
    print("Todas las columnas necesarias están presentes.")

# Mostrar categorías únicas para depuración
print("\nCategorías únicas en 'categoria_del_producto':", tienda['categoria_del_producto'].unique().tolist())

# ----------------------------------------------
# FILTRADO DE DATOS (¡Filtro de Electrodomésticos Arreglado!)
# ----------------------------------------------

# 1. Mostrar todas las filas donde el precio sea mayor a 500000
productos_caros = tienda[tienda['precio'] > 500000]
print("\nProductos con precio mayor a 500000 (primeras 5 filas):")
print(productos_caros.head())

# 2. Filtrar productos que sean de la categoría "Electrodomésticos"
electrodomesticos = tienda[tienda['categoria_del_producto'] == "Electrodomésticos"]
print("\nProductos de la categoría 'Electrodomésticos' (primeras 5 filas):")
print(electrodomesticos.head())

# 3. Filtrar productos con precio mayor a 500000 **y** de la categoría "Electrodomésticos"
caros_electrodomesticos = tienda[
    (tienda['precio'] > 500000) &
    (tienda['categoria_del_producto'] == "Electrodomésticos")
]
print("\nProductos de 'Electrodomésticos' con precio mayor a 500000 (primeras 5 filas):")
print(caros_electrodomesticos.head())

# 4. Filtrar productos con precio menor o igual a 50000 **o** que sean de la categoría "Muebles"
baratos_o_muebles = tienda[
    (tienda['precio'] <= 50000) |
    (tienda['categoria_del_producto'] == "Muebles")
]
print("\nProductos con precio <= 50000 o de la categoría 'Muebles' (primeras 5 filas):")
print(baratos_o_muebles.head())

# 5. Filtrar productos cuyo nombre contenga la palabra "cable" (sin importar mayúsculas)
productos_cable = tienda[tienda['producto'].str.contains("cable", case=False, na=False)]
print("\nProductos que contienen 'cable' en el nombre (primeras 5 filas):")
print(productos_cable.head())

# 6. Mostrar solo columnas específicas
solo_nombre_precio = tienda[['producto', 'precio']]
print("\nVista simplificada con solo producto y precio (primeras 5 filas):")
print(solo_nombre_precio.head())

'''
(venv) ┌──(venv)─(pol㉿kali)-[~/Escritorio/Alura_practicas_ds]
└─$ /home/pol/Escritorio/Alura_practicas_ds/venv/bin/python /home/pol/Escritorio/Alura_practicas_ds/practica_1.py
Columnas disponibles: ['producto', 'categoria_del_producto', 'precio', 'costo_de_envio', 'fecha_de_compra', 'vendedor', 'lugar_de_compra', 'calificacion', 'metodo_de_pago', 'cantidad_de_cuotas', 'lat', 'lon']
Todas las columnas necesarias están presentes.

Categorías únicas en 'categoria_del_producto': ['Electrónicos', 'Muebles', 'Juguetes', 'Electrodomésticos', 'Artículos para el hogar', 'Deportes y diversión', 'Libros', 'Instrumentos musicales']

Productos con precio mayor a 500000 (primeras 5 filas):
            producto categoria_del_producto     precio  ...  cantidad_de_cuotas       lat       lon
3         Microondas      Electrodomésticos   757500.0  ...                   1   3.43722 -76.52250
7       Lavavajillas      Electrodomésticos  1189700.0  ...                  10  11.24079 -74.19904
8   Lavadora de ropa      Electrodomésticos  1518200.0  ...                   5   4.60971 -74.08175
10      Refrigerador      Electrodomésticos  2431300.0  ...                   2   4.60971 -74.08175
11      Lavavajillas      Electrodomésticos  1417100.0  ...                   1  10.39972 -75.51444

[5 rows x 12 columns]

Productos de la categoría 'Electrodomésticos' (primeras 5 filas):
            producto categoria_del_producto     precio  ...  cantidad_de_cuotas       lat       lon
3         Microondas      Electrodomésticos   757500.0  ...                   1   3.43722 -76.52250
7       Lavavajillas      Electrodomésticos  1189700.0  ...                  10  11.24079 -74.19904
8   Lavadora de ropa      Electrodomésticos  1518200.0  ...                   5   4.60971 -74.08175
10      Refrigerador      Electrodomésticos  2431300.0  ...                   2   4.60971 -74.08175
11      Lavavajillas      Electrodomésticos  1417100.0  ...                   1  10.39972 -75.51444

[5 rows x 12 columns]

Productos de 'Electrodomésticos' con precio mayor a 500000 (primeras 5 filas):
            producto categoria_del_producto     precio  ...  cantidad_de_cuotas       lat       lon
3         Microondas      Electrodomésticos   757500.0  ...                   1   3.43722 -76.52250
7       Lavavajillas      Electrodomésticos  1189700.0  ...                  10  11.24079 -74.19904
8   Lavadora de ropa      Electrodomésticos  1518200.0  ...                   5   4.60971 -74.08175
10      Refrigerador      Electrodomésticos  2431300.0  ...                   2   4.60971 -74.08175
11      Lavavajillas      Electrodomésticos  1417100.0  ...                   1  10.39972 -75.51444

[5 rows x 12 columns]

Productos con precio <= 50000 o de la categoría 'Muebles' (primeras 5 filas):
                   producto categoria_del_producto    precio  ...  cantidad_de_cuotas       lat       lon
1           Mesa de comedor                Muebles  192300.0  ...                   4   6.25184 -75.56359
4          Silla de oficina                Muebles  335200.0  ...                   1   6.25184 -75.56359
5   Bloques de construcción               Juguetes   24200.0  ...                   1   3.43722 -76.52250
6               Muñeca bebé               Juguetes   44200.0  ...                   1   4.60971 -74.08175
17        Ajedrez de madera               Juguetes   29600.0  ...                   2  11.24079 -74.19904

[5 rows x 12 columns]

Productos que contienen 'cable' en el nombre (primeras 5 filas):
Empty DataFrame
Columns: [producto, categoria_del_producto, precio, costo_de_envio, fecha_de_compra, vendedor, lugar_de_compra, calificacion, metodo_de_pago, cantidad_de_cuotas, lat, lon]
Index: []

Vista simplificada con solo producto y precio (primeras 5 filas):
            producto    precio
0  Asistente virtual  164300.0
1    Mesa de comedor  192300.0
2      Juego de mesa  209600.0
3         Microondas  757500.0
4   Silla de oficina  335200.0
'''