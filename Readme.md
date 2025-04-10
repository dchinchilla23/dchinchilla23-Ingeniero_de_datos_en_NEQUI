# Proyecto de Detección de Fraude en Transacciones con Tarjeta de Crédito

## Alcance del Proyecto
Este proyecto tiene como objetivo construir una canalización de datos (ETL) para:
- **Captura y almacenamiento:** Recopilar datos de transacciones de tarjetas de crédito desde un dataset público.
- **Procesamiento y limpieza:** Detectar y gestionar datos duplicados, valores perdidos y problemas de formatos.
- **Modelado para detección de fraudes:** Utilizar técnicas de machine learning para identificar transacciones fraudulentas.
- **Generación de reportes y dashboards:** Proveer un sistema de análisis que informe patrones de gasto y alertas de fraude.

## Datos Utilizados
- **Dataset:** Massive Bank dataset ( 1 Million+ rows)  
  [Link al dataset](https://www.kaggle.com/datasets/ksabishek/massive-bank-dataset-1-million-rows)
- **Características:**  
  - **Transacciones totales:** 1004480  
## Casos de Uso
1. **1.	Análisis exploratorio y reportes.:**  
   Comprender los patrones de comportamientos financieros por categoría ( Domain), ubicación(location) y volumnes de transacciones.
   Uso. Cracion de reportes interactivos o dashboards con herramientas de power bi table o amazon quiksigt
.
2. **2.	Detección de fraude:**  
   Identificar patrones en dominios, ubicaciones, y frecuencias de transacciones.
   Uso. Generar alertas tempranas para posibles fraudes bancarios

3. **3.	Análisis de datos. :**  
   Construcción de una bd como fuente de verdad analítica para la creación de dashboards donde muestre en comportamiento de sectores y regiones la cual servirá como referencia para futuros análisis o auditorias
4. **4.	Automatización en nube:**  
   Pensado para poder ejecutarse en pipelines automáticos en aws(glue, s3, athena,Redshift)


## Herramientas y Tecnologías
- **Lenguaje:** Python
- **Framework ETL:** Pandas, SQLAlchemy (para interacción con base de datos)
- **Documentación:** Markdown (README.md) y diagramas (arquitectura_aws.drawio) Documento de ejecucion(Word)

# Librerias a instalar
 el archivo .env contiene la configuracion de python necesaria para el proyecto
- **Lenguaje:** Python 3.13

## Librerias
- Pandas
- shutil
- kagglehub
- sqlalchemy psycopg2-binary
