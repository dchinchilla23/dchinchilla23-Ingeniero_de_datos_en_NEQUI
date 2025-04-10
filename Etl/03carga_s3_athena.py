import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexion-
usuario = 'tu_usuario'
contraseña = 'tu_contraseña'
host = 'nombre.rds.amazonaws.com'
puerto = '5432'
base_datos = 'fraud_detection'

# Crear motor de conexion-
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}')

# Leer el archivo procesado
df = pd.read_csv("Fuente/Procesados/bank_flagged_simple.csv")

# Cargar a RDS
df.to_sql('transacciones_bancarias', engine, if_exists='replace', index=False)
print("✅ Datos cargados en Amazon RDS (PostgreSQL)")
