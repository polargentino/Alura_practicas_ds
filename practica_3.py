'''
Análisis Exploratorio de Datos (EDA)! 🔍📊
Te voy a preparar un bloque completo que incluya:

Producto más vendido

Categoría con más ventas

Categoría con mayor ticket promedio

Top ciudades con más compras

Estadísticas generales de precios
'''
import pandas as pd
import unicodedata

# Función para normalizar texto (quita acentos, convierte a minúsculas, reemplaza espacios)
def normalize_text(text):
    if pd.isnull(text): return ""
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

# Renombrar columnas
tienda.columns = [normalize_text(col) for col in tienda.columns]
print("🧠 Columnas disponibles:", tienda.columns.tolist())

# Eliminar duplicados
duplicados = tienda.duplicated().sum()
tienda = tienda.drop_duplicates()
print(f"\n🧹 Duplicados eliminados: {duplicados}")

# Eliminar filas con nulos en columnas críticas
columnas_criticas = ['producto', 'categoria_del_producto', 'precio', 'fecha_de_compra']
tienda = tienda.dropna(subset=columnas_criticas)
print(f"📉 Filas después de eliminar nulos críticos: {tienda.shape[0]}")

# Normalizar categorías
tienda['categoria_del_producto'] = tienda['categoria_del_producto'].apply(normalize_text)
print("\n🏷️ Categorías únicas después de normalizar:")
print(tienda['categoria_del_producto'].unique())

# ---------- ANÁLISIS EXPLORATORIO ----------

df = tienda  # para mantener consistencia con tu código anterior

print("\n🔍 Dimensiones del DataFrame:", df.shape)
print("\n📦 Columnas disponibles:", df.columns.tolist())

# 1. Producto más vendido
producto_mas_vendido = df['producto'].value_counts().idxmax()
cantidad_ventas_producto_top = df['producto'].value_counts().max()
print(f"\n🏆 Producto más vendido: {producto_mas_vendido} ({cantidad_ventas_producto_top} ventas)")

# 2. Categoría con más ventas
categoria_top = df['categoria_del_producto'].value_counts().idxmax()
ventas_categoria_top = df['categoria_del_producto'].value_counts().max()
print(f"📂 Categoría más vendida: {categoria_top} ({ventas_categoria_top} ventas)")

# 3. Categoría con ticket promedio más alto
ticket_promedio_por_categoria = df.groupby('categoria_del_producto')['precio'].mean().sort_values(ascending=False)
print("\n💰 Ticket promedio por categoría (ordenado):")
print(ticket_promedio_por_categoria)

# 4. Top 5 ciudades con más compras
top_ciudades = df['lugar_de_compra'].value_counts().head(5)
print("\n🌆 Top 5 ciudades con más compras:")
print(top_ciudades)

# 5. Estadísticas generales del precio
print("\n📈 Estadísticas generales del precio:")
print(df['precio'].describe())


'''
🧠 Columnas disponibles: ['producto', 'categoria_del_producto', 'precio', 'costo_de_envio', 'fecha_de_compra', 'vendedor', 'lugar_de_compra', 'calificacion', 'metodo_de_pago', 'cantidad_de_cuotas', 'lat', 'lon']

🧹 Duplicados eliminados: 0
📉 Filas después de eliminar nulos críticos: 2359

🏷️ Categorías únicas después de normalizar:
['electronicos' 'muebles' 'juguetes' 'electrodomesticos'
 'articulos_para_el_hogar' 'deportes_y_diversion' 'libros'
 'instrumentos_musicales']

🔍 Dimensiones del DataFrame: (2359, 12)

📦 Columnas disponibles: ['producto', 'categoria_del_producto', 'precio', 'costo_de_envio', 'fecha_de_compra', 'vendedor', 'lugar_de_compra', 'calificacion', 'metodo_de_pago', 'cantidad_de_cuotas', 'lat', 'lon']

🏆 Producto más vendido: TV LED UHD 4K (60 ventas)
📂 Categoría más vendida: muebles (465 ventas)

💰 Ticket promedio por categoría (ordenado):
categoria_del_producto
electrodomesticos          1.165658e+06
electronicos               9.586908e+05
instrumentos_musicales     5.016429e+05
muebles                    4.035133e+05
deportes_y_diversion       1.383451e+05
articulos_para_el_hogar    7.425965e+04
juguetes                   5.554228e+04
libros                     5.077977e+04
Name: precio, dtype: float64

🌆 Top 5 ciudades con más compras:
lugar_de_compra
Bogotá          984
Medellín        563
Cali            283
Pereira         133
Barranquilla     75
Name: count, dtype: int64

📈 Estadísticas generales del precio:
count    2.359000e+03
mean     4.878679e+05
std      6.146868e+05
min      7.600000e+03
25%      5.575000e+04
50%      2.353000e+05
75%      6.781000e+05
max      2.977000e+06
Name: precio, dtype: float64
'''
