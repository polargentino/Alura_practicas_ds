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

'''
(venv) ┌──(venv)─(pol㉿kali)-[~/Escritorio/Alura_practicas_ds]
└─$ /home/pol/Escritorio/Alura_practicas_ds/venv/bin/python /home/pol/Escritorio/Alura_practicas_ds/practica.py
Forma del DataFrame (filas, columnas):
(2359, 12)

Nombre de las columnas:
Index(['Producto', 'Categoría del Producto', 'Precio', 'Costo de envío',
       'Fecha de Compra', 'Vendedor', 'Lugar de Compra', 'Calificación',
       'Método de pago', 'Cantidad de cuotas', 'lat', 'lon'],
      dtype='object')

Primeras 5 filas:
            Producto Categoría del Producto    Precio  ...  Cantidad de cuotas       lat       lon
0  Asistente virtual           Electrónicos  164300.0  ...                   8   4.60971 -74.08175
1    Mesa de comedor                Muebles  192300.0  ...                   4   6.25184 -75.56359
2      Juego de mesa               Juguetes  209600.0  ...                   1  10.39972 -75.51444
3         Microondas      Electrodomésticos  757500.0  ...                   1   3.43722 -76.52250
4   Silla de oficina                Muebles  335200.0  ...                   1   6.25184 -75.56359

[5 rows x 12 columns]

Últimas 5 filas:
           Producto Categoría del Producto     Precio  ...  Cantidad de cuotas      lat       lon
2354      Iphone 15           Electrónicos  1284400.0  ...                   1  6.25184 -75.56359
2355      Impresora           Electrónicos   282800.0  ...                   1  4.60971 -74.08175
2356  Juego de mesa               Juguetes   122900.0  ...                   4  3.43722 -76.52250
2357       Cama box                Muebles   691300.0  ...                   2  1.21361 -77.28111
2358     Smartwatch           Electrónicos   195000.0  ...                   1  3.43722 -76.52250

[5 rows x 12 columns]

Información general del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2359 entries, 0 to 2358
Data columns (total 12 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   Producto                2359 non-null   object 
 1   Categoría del Producto  2359 non-null   object 
 2   Precio                  2359 non-null   float64
 3   Costo de envío          2359 non-null   float64
 4   Fecha de Compra         2359 non-null   object 
 5   Vendedor                2359 non-null   object 
 6   Lugar de Compra         2359 non-null   object 
 7   Calificación            2359 non-null   int64  
 8   Método de pago          2359 non-null   object 
 9   Cantidad de cuotas      2359 non-null   int64  
 10  lat                     2359 non-null   float64
 11  lon                     2359 non-null   float64
dtypes: float64(4), int64(2), object(6)
memory usage: 221.3+ KB
None

Estadísticas básicas:
             Precio  Costo de envío  Calificación  Cantidad de cuotas          lat          lon
count  2.359000e+03     2359.000000   2359.000000         2359.000000  2359.000000  2359.000000
mean   4.878679e+05    26018.609580      3.976685            2.943196     5.365283   -74.789417
std    6.146868e+05    32860.001783      1.415370            2.819897     2.287445     1.217827
min    7.600000e+03        0.000000      1.000000            1.000000    -4.215280   -77.281110
25%    5.575000e+04     3100.000000      3.000000            1.000000     4.609710   -75.563590
50%    2.353000e+05    12400.000000      5.000000            1.000000     4.609710   -74.199040
75%    6.781000e+05    36000.000000      5.000000            4.000000     6.251840   -74.081750
max    2.977000e+06   160800.000000      5.000000           24.000000    11.544440   -67.923900

Valores nulos por columna:
Producto                  0
Categoría del Producto    0
Precio                    0
Costo de envío            0
Fecha de Compra           0
Vendedor                  0
Lugar de Compra           0
Calificación              0
Método de pago            0
Cantidad de cuotas        0
lat                       0
lon                       0
dtype: int64
'''