'''
🐍 practica_4.py COMPLETO CON VISUALIZACIONES:
✅ Usa tu limpieza y normalización original.
✅ Incluye gráficos de:

Top 5 productos más vendidos

Cantidad de productos por categoría

Ticket promedio por categoría

Top 5 ciudades con más compras
✅ Guarda los gráficos como imágenes .png.



'''
import pandas as pd
import unicodedata
import seaborn as sns
import matplotlib.pyplot as plt

# Función para normalizar texto (quita acentos, convierte a minúsculas, reemplaza espacios)
def normalize_text(text):
    if pd.isnull(text): return ""
    return ''.join(
        c for c in unicodedata.normalize('NFD', str(text))
        if unicodedata.category(c) != 'Mn'
    ).lower().replace(" ", "_")

# Cargar archivo CSV desde GitHub
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
df = tienda

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

# 3. Ticket promedio por categoría
ticket_promedio_por_categoria = df.groupby('categoria_del_producto')['precio'].mean().sort_values(ascending=False)
print("\n💰 Ticket promedio por categoría:")
print(ticket_promedio_por_categoria)

# 4. Top 5 ciudades con más compras
top_ciudades = df['lugar_de_compra'].value_counts().head(5)
print("\n🌆 Top 5 ciudades con más compras:")
print(top_ciudades)

# 5. Estadísticas generales del precio
print("\n📈 Estadísticas generales del precio:")
print(df['precio'].describe())

# ---------- GRÁFICOS ----------

sns.set_theme(style="whitegrid")

# Gráfico 1: Top 5 productos más vendidos
top5_productos = df['producto'].value_counts().head(5)
sns.barplot(x=top5_productos.values, y=top5_productos.index, palette='Blues_r')
plt.title("Top 5 productos más vendidos")
plt.xlabel("Cantidad de ventas")
plt.tight_layout()
plt.savefig("grafico_top5_productos.png")
plt.close()

# Gráfico 2: Cantidad de productos por categoría
sns.countplot(
    y='categoria_del_producto',
    data=df,
    order=df['categoria_del_producto'].value_counts().index,
    palette='pastel'
)
plt.title("Cantidad de productos por categoría")
plt.xlabel("Cantidad")
plt.tight_layout()
plt.savefig("grafico_categorias.png")
plt.close()

# Gráfico 3: Ticket promedio por categoría
ticket_promedio_por_categoria.plot(kind='barh', color='salmon')
plt.title("Ticket promedio por categoría")
plt.xlabel("Precio promedio")
plt.tight_layout()
plt.savefig("grafico_ticket_promedio.png")
plt.close()

# Gráfico 4: Top ciudades con más compras
sns.barplot(x=top_ciudades.values, y=top_ciudades.index, palette='Greens_d')
plt.title("Top 5 ciudades con más compras")
plt.xlabel("Cantidad de compras")
plt.tight_layout()
plt.savefig("grafico_top5_ciudades.png")
plt.close()
