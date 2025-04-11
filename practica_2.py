'''
🧹 3. Limpieza de Datos con pandas
¿Qué vas a aprender en este bloque?

Cómo tratar valores nulos (NaN).

Cómo eliminar duplicados.

Cómo corregir errores en texto (por ejemplo, normalizar categorías).

Cómo transformar tipos de datos si es necesario.
'''
import pandas as pd
import unicodedata

# Función para normalizar texto (quitar acentos y convertir a minúsculas con guiones bajos)
def normalize_text(text):
    if pd.isnull(text): return ""  # Evitar errores con NaN
    return ''.join(
        c for c in unicodedata.normalize('NFD', str(text))
        if unicodedata.category(c) != 'Mn'
    ).lower().replace(" ", "_")

# Cargar el archivo CSV
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
try:
    tienda = pd.read_csv(url)
except Exception as e:
    print(f"❌ Error al cargar el archivo: {e}")
    exit()

# Normalizar nombres de columnas
tienda.columns = [normalize_text(col.strip()) for col in tienda.columns]
print("🧠 Columnas disponibles:", tienda.columns.tolist())

# ✅ Revisión de valores nulos
print("\n🔍 Conteo de valores nulos por columna:")
print(tienda.isnull().sum())

# ✅ Eliminación de duplicados
filas_antes = tienda.shape[0]
tienda = tienda.drop_duplicates()
filas_despues = tienda.shape[0]
print(f"\n🧹 Duplicados eliminados: {filas_antes - filas_despues}")

# ✅ Eliminar filas con valores nulos importantes (por ejemplo: producto o precio)
tienda = tienda.dropna(subset=['producto', 'precio'])
print(f"📉 Filas después de eliminar nulos críticos: {tienda.shape[0]}")

# ✅ Corregir errores en la categoría (espacios, acentos, mayúsculas)
tienda['categoria_del_producto'] = tienda['categoria_del_producto'].apply(normalize_text)

# ✅ Ver categorías únicas después de normalizar
print("\n🏷️ Categorías únicas después de normalizar:")
print(sorted(tienda['categoria_del_producto'].unique()))

# ✅ Asegurar que el tipo de dato de 'precio' sea numérico
tienda['precio'] = pd.to_numeric(tienda['precio'], errors='coerce')

# ✅ Eliminar nuevamente posibles NaN creados por conversiones
tienda = tienda.dropna(subset=['precio'])

# ✅ Resetear el índice después de limpiezas
tienda.reset_index(drop=True, inplace=True)

print("\n✅ Limpieza completa. DataFrame listo para análisis.")
print(tienda.head())

'''
🧠 Columnas disponibles: ['producto', 'categoria_del_producto', 'precio', 'costo_de_envio', 'fecha_de_compra', 'vendedor', 'lugar_de_compra', 'calificacion', 'metodo_de_pago', 'cantidad_de_cuotas', 'lat', 'lon']

🔍 Conteo de valores nulos por columna:
producto                  0
categoria_del_producto    0
precio                    0
costo_de_envio            0
fecha_de_compra           0
vendedor                  0
lugar_de_compra           0
calificacion              0
metodo_de_pago            0
cantidad_de_cuotas        0
lat                       0
lon                       0
dtype: int64

🧹 Duplicados eliminados: 0
📉 Filas después de eliminar nulos críticos: 2359

🏷️ Categorías únicas después de normalizar:
['articulos_para_el_hogar', 'deportes_y_diversion', 'electrodomesticos', 'electronicos', 'instrumentos_musicales', 'juguetes', 'libros', 'muebles']

✅ Limpieza completa. DataFrame listo para análisis.
            producto categoria_del_producto    precio  ...  cantidad_de_cuotas       lat       lon
0  Asistente virtual           electronicos  164300.0  ...                   8   4.60971 -74.08175
1    Mesa de comedor                muebles  192300.0  ...                   4   6.25184 -75.56359
2      Juego de mesa               juguetes  209600.0  ...                   1  10.39972 -75.51444
3         Microondas      electrodomesticos  757500.0  ...                   1   3.43722 -76.52250
4   Silla de oficina                muebles  335200.0  ...                   1   6.25184 -75.56359

[5 rows x 12 columns]
                     
'''
