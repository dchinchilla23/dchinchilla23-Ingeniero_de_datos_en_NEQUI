import pandas as pd
import sys

# Ruta completa del archivo xlsx como argumento
excel_path = sys.argv[1]

# Leer el Excel
df = pd.read_excel(excel_path)

# Imprimir CSV como salida estándar (stdout)
print(df.to_csv(index=False))
