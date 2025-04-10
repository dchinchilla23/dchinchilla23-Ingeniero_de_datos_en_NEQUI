import os
import shutil
import kagglehub
import pandas as pd
# Descargar el dataset desde kaggle
path = kagglehub.dataset_download("ksabishek/massive-bank-dataset-1-million-rows")
print("✅ Dataset descargado en:", path)

# Ruta al directorio "Fuente" dentro del directorio actual
current_dir = os.getcwd()
fuente_dir = os.path.join(current_dir, "Fuente")

# Crear el directorio Fuente si no existe
os.makedirs(fuente_dir, exist_ok=True)

# Copiar archivos del dataset a la carpeta Fuente
for root, dirs, files in os.walk(path):
    for file in files:
        source = os.path.join(root, file)
        destination = os.path.join(fuente_dir, file)
        shutil.copy2(source, destination)
        print(f"📂 Copiado: {file} -> {fuente_dir}")

print("✅ Todos los archivos fueron copiados a la carpeta 'Fuente'.")

try:
    # Lee el archivo Excel en un DataFrame de pandas.
    df = pd.read_excel('Fuente\\bankdataset.xlsx')

    # Muestra los primeros 10 registros del DataFrame
    print("Primeros 10 registros del archivo bankdataset.xlsx:")
    print(df.head(10))

    # Informacion del df:
    print("\nInformación del DataFrame:")
    print(df.info())

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{'Fuente\\bankdataset.xlsx'}' ")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo Excel: {e}")