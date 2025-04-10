import pandas as pd
# # ------------------------------#############-----------------------#
# # Análisis de calidad de datos                                      #
# # ------------------------------------------------------------------#
class BankDataCleaner:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def cargar_datos(self):
        print(f" Cargando datos desde: {self.input_path}")
        self.df = pd.read_excel(self.input_path)

    def analizar_calidad(self):
        print(" Información general del dataset:")
        print(self.df.info())

        print("\n Primeras filas:")
        print(self.df.head())

        print("\n Estadísticas descriptivas:")
        print(self.df.describe(include='all'))

        print("\n Valores nulos por columna:")
        print(self.df.isnull().sum())

        print("\n Registros duplicados:")
        print(self.df.duplicated().sum())

    def limpiar_datos(self):
        print("\n Eliminando duplicados exactos...")
        self.df = self.df.drop_duplicates()
        print(f"Duplicados después de limpieza: {self.df.duplicated().sum()}")

        print("\n Formateando columna de fechas...")
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        print("\n Validando columnas numericas...")
        self.df['Value'] = pd.to_numeric(self.df['Value'], errors='coerce')
        self.df['Transaction_count'] = pd.to_numeric(self.df['Transaction_count'], errors='coerce')

        print("\n Estandarizando campos de texto (Domain y Location)...")
        self.df['Domain'] = self.df['Domain'].str.upper().str.strip()
        self.df['Location'] = self.df['Location'].str.upper().str.strip()

    def guardar_datos(self):
        print(f"\n Guardando dataset limpio en: {self.output_path}")
        self.df.to_csv(self.output_path, index=False)
        print(" Dataset limpio guardado exitosamente.")

    def ejecutar(self):
        self.cargar_datos()
        self.analizar_calidad()
        self.limpiar_datos()
        self.guardar_datos()

# ------------------------------
# Uso del script
# ------------------------------
if __name__ == "__main__":
    input_path = "Fuente/bankdataset.xlsx"
    output_path = "Fuente/Procesados/bank_cleaned.csv"

    limpiador = BankDataCleaner(input_path, output_path)
    limpiador.ejecutar()
