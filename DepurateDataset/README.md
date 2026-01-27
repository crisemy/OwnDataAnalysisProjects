# Data Cleaning Script (`depurateDataSetScript.py`)

Este repositorio incluye el script `depurateDataSetScript.py`, una herramienta interactiva para limpiar datasets en Python utilizando la librería `pandas`.

## ¿Qué hace el script?

- Permite al usuario seleccionar diferentes pasos de limpieza para aplicar al dataset.
- Es flexible y puede adaptarse a distintos datasets con modificaciones mínimas.
- Incluye inspección inicial y final del dataset para visualizar cambios.

## Pasos de limpieza disponibles

1. **Manejar valores faltantes:** Rellena o elimina valores nulos en columnas clave.
2. **Eliminar duplicados:** Elimina filas duplicadas, especialmente por identificadores únicos.
3. **Convertir tipos de datos:** Ajusta el tipo de datos de columnas relevantes.
4. **Renombrar columnas:** Renombra columnas comunes para mayor claridad.
5. **Limpiar strings:** Normaliza y limpia valores de texto.
6. **Manejar outliers:** Filtra valores atípicos en columnas numéricas.
7. **Codificar categóricas:** Aplica one-hot encoding a variables categóricas.
8. **Eliminar columnas innecesarias:** Elimina columnas que no aportan valor al análisis.

## Uso

1. Instala pandas si no lo tienes:
   ```
   pip install pandas
   ```
2. Ejecuta el script:
   ```
   python depurateDataSetScript.py
   ```
3. Ingresa la URL o ruta local del archivo CSV (por defecto usa el Titanic dataset).
4. Selecciona los pasos de limpieza que deseas aplicar.
5. El dataset limpio se guarda en el archivo que indiques (por defecto `cleaned.csv`).

## Ejemplo de dataset

- [Titanic dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

## Autor
crisemy@gmail.com