import pandas as pd

class FraudRuleBasedDetector:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def cargar_datos(self):
        print(f"Cargando dataset limpio desde: {self.input_path}")
        self.df = pd.read_csv(self.input_path)

    def aplicar_reglas_de_fraude(self):
        print("Aplicando reglas simples basadas en estadisticos...")

        # Calcular estadísticas por Domain
        domain_stats = self.df.groupby('Domain')[['Value', 'Transaction_count']].agg(['mean', 'std']).reset_index()
        domain_stats.columns = ['Domain', 'Value_mean', 'Value_std', 'Tx_mean', 'Tx_std']

        # Unir estadisticas  al dataset original
        self.df = self.df.merge(domain_stats, on='Domain', how='left')

        # Z-score para valor y numero ero de transacciones 
        self.df['anomaly_value'] = ((self.df['Value'] - self.df['Value_mean']) / self.df['Value_std']).abs() > 2
        self.df['anomaly_tx'] = ((self.df['Transaction_count'] - self.df['Tx_mean']) / self.df['Tx_std']).abs() > 2

        # Flag de sospecha 
        self.df['fraude_simple'] = ((self.df['anomaly_value']) | (self.df['anomaly_tx'])).astype(int)

    def guardar_resultados(self):
        self.df.to_csv(self.output_path, index=False)
        print(f"*** Resultados guardados en: {self.output_path}")
        print("*** Conteo de transacciones sospechosas:")
        print(self.df['fraude_simple'].value_counts())

    def ejecutar(self):
        self.cargar_datos()
        self.aplicar_reglas_de_fraude()
        self.guardar_resultados()

# ------------------------------
# Uso del script
# ------------------------------
if __name__ == "__main__":
    entrada = "Fuente/Procesados/bank_cleaned.csv"
    salida = "Fuente/Procesados/bank_flagged_simple.csv"

    detector = FraudRuleBasedDetector(entrada, salida)
    detector.ejecutar()
