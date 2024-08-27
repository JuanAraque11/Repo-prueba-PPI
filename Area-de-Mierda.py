import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Leer las primeras líneas del archivo como texto plano
print("Primeras líneas del archivo:")
with open('Materiales/Semillero/DatosEnsayo_1_csv.csv', 'r', encoding='utf-8-sig') as file:
    for _ in range(10):
        print(file.readline().strip())
print("\n" + "="*50 + "\n")

# Paso 2: Leer una muestra del archivo sin procesar
print("Muestra de 10 filas del archivo sin procesar:")
df_sample = pd.read_csv('Materiales/Semillero/DatosEnsayo_1_csv.csv', 
                        sep=';',
                        encoding='utf-8-sig',
                        nrows=10)
print(df_sample)
print("\n" + "="*50 + "\n")

# Paso 3: Leer y procesar el archivo completo
print("Procesamiento del archivo completo:")
df = pd.read_csv('Materiales/Semillero/DatosEnsayo_1_csv.csv', 
                 sep=';',
                 encoding='utf-8-sig',
                 decimal=',',
                 thousands='.',
                 header=0)

# Convertir a numérico y eliminar filas no numéricas
df = df.apply(pd.to_numeric, errors='coerce').dropna()

# Calcular la tenacidad
tenacidad = np.trapz(df['Esfuerzo de compresión'], df['Deformación por compresión'])

print(f"Tenacidad calculada: {tenacidad:.4f} MPa")
print("\nPrimeras 5 filas del DataFrame procesado:")
print(df.head())
print("\nÚltimas 5 filas del DataFrame procesado:")
print(df.tail())
print("\nInformación del DataFrame:")
print(df.info())

# Graficar una muestra de los datos
plt.figure(figsize=(10, 6))
sample_size = min(1000, len(df))
df_sample = df.sample(n=sample_size)
plt.plot(df_sample['Deformación por compresión'], df_sample['Esfuerzo de compresión'], 'b.', alpha=0.5)
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Muestra de la Curva Esfuerzo-Deformación')
plt.grid(True)
plt.show()