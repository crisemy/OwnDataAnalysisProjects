## El objetivo de este script es proporcionar una herramienta interactiva para limpiar datasets en Python
## El usuario puede seleccionar diferentes pasos de limpieza y el script aplicará esos pasos al dataset
## El script está diseñado para ser flexible y puede adaptarse a diferentes datasets con modificaciones mínimas
## Requiere pandas: pip install pandas
## Uso: python depurateDataSetScript.py
## Dataset de ejemplo: Titanic dataset (https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
## Autor: crisemy@gmail.com

import pandas as pd

# Leer el dataset de una URL o archivo local
def load_data(file_path):
    return pd.read_csv(file_path) # Cambiar a pd.read_excel() si es un archivo Excel. titanic.csv

# Inspeccionar el dataset
def inspect_data(df):
    print("\nInformación del dataset:")
    print(df.info())
    print("\nEstadísticas descriptivas:")
    print(df.describe())
    print("\nValores faltantes:")
    print(df.isnull().sum())

# Funciones de limpieza
# Modificar estas funciones según las necesidades del dataset específico en base a sus propiedades
def handle_missing_values(df):
    # Rellena 'Age' con mediana, elimina NaN en 'Embarked'
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
    if 'Embarked' in df.columns:
        df = df.dropna(subset=['Embarked'])
    return df

# Eliminar duplicados
def remove_duplicates(df):
    # Elimina duplicados por 'PassengerId' si existe
    if 'PassengerId' in df.columns:
        df = df.drop_duplicates(subset=['PassengerId'])
    else:
        df = df.drop_duplicates()
    return df

# Convertir tipos de datos
def convert_data_types(df):
    # Convierte 'Age' a float si existe
    if 'Age' in df.columns:
        df['Age'] = df['Age'].astype(float)
    return df

# Renombrar columnas
def rename_columns(df):
    # Renombra columnas comunes
    rename_dict = {'Pclass': 'PassengerClass', 'SibSp': 'SiblingsSpouses'}
    df = df.rename(columns={k: v for k, v in rename_dict.items() if k in df.columns})
    return df

# Limpiar strings
def clean_strings(df):
    # Limpia 'Sex' y 'Name' si existen
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].str.strip().str.lower()
    if 'Name' in df.columns:
        df['Name'] = df['Name'].str.replace(r'\(.*\)', '', regex=True)
    return df

# Manejar outliers
def handle_outliers(df):
    # Maneja outliers en 'Fare' si existe
    if 'Fare' in df.columns:
        Q1 = df['Fare'].quantile(0.25)
        Q3 = df['Fare'].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df['Fare'] >= (Q1 - 1.5 * IQR)) & (df['Fare'] <= (Q3 + 1.5 * IQR))]
    return df

# Codificar variables categóricas
def encode_categorical(df):
    # One-hot encoding para 'Sex' y 'Embarked' si existen
    cat_cols = [col for col in ['Sex', 'Embarked'] if col in df.columns]
    if cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df

# Eliminar columnas innecesarias
def drop_unnecessary_columns(df):
    # Elimina 'Cabin' y 'Ticket' si existen
    drop_cols = [col for col in ['Cabin', 'Ticket'] if col in df.columns]
    if drop_cols:
        df = df.drop(columns=drop_cols)
    return df
# Guardar el dataset limpio en un path especifico
def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\nDataset limpio guardado en: {output_path}")

# Menú principal
def main():
    file_path = input("Ingresa la URL o path del CSV (default: Titanic): ") or "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = load_data(file_path)
    
    inspect_data(df)  # Inspección inicial siempre
    
    options = {
        '1': handle_missing_values,
        '2': remove_duplicates,
        '3': convert_data_types,
        '4': rename_columns,
        '5': clean_strings,
        '6': handle_outliers,
        '7': encode_categorical,
        '8': drop_unnecessary_columns
    }
    
    print("\nSelecciona pasos de limpieza (separados por coma, e.g., 1,3,5):")
    print("1: Manejar valores faltantes")
    print("2: Eliminar duplicados")
    print("3: Convertir tipos de datos")
    print("4: Renombrar columnas")
    print("5: Limpiar strings")
    print("6: Manejar outliers")
    print("7: Codificar categóricas")
    print("8: Eliminar columnas innecesarias")
    print("0: Salir sin cambios")
    
    selected = input("Opciones: ").split(',')
    
    for opt in selected:
        opt = opt.strip()
        if opt in options:
            df = options[opt](df)
            print(f"Paso {opt} aplicado.")
    
    if selected and '0' not in selected:
        output_path = input("Nombre del archivo de salida (default: cleaned.csv): ") or "cleaned.csv"
        save_data(df, output_path)
        inspect_data(df)  # Inspección final
        print("Proceso de depuración completado")

if __name__ == "__main__":
    main()