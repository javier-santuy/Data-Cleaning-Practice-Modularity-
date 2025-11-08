
import pandas as pd
import numpy as np

#Sustituir valores incorrectos por nulos
def clean_na_values(df):
    valores_a_buscar = [
    'error', 'Error', 'ERROR', 
    'unknown', 'Unknown', 'UNKNOWN',
    'NaN', 'NAN', 'N/A', '',]
    df_transformed = df.replace( 
        to_replace=valores_a_buscar,
        value = np.nan,
        regex=False
)
    return df_transformed

def drop_duplicaciones(df: pd.DataFrame) -> pd.DataFrame:
    
    """Elimina filas duplicadas en el DataFrame."""
    total_eliminados = df.duplicated().sum()
    df_limpio = df.drop_duplicates()
    if total_eliminados > 0:
        print(f"🗑️ Duplicados eliminados: {total_eliminados}")
    else:
        print("No hay valores duplicados en los datos")
    return df_limpio



def contar_valores_especificos(columna: pd.Series, valores: list) -> dict:
    """
    Cuenta la frecuencia de aparición de cada valor de la lista en una columna.
    """
    # Convertir a mayúsculas para conteo insensible a mayúsculas/minúsculas
    columna_upper = columna.astype(str).str.upper()
    valores_upper = [v.upper() for v in valores]
    
    # Crear un diccionario para almacenar los conteos
    conteo_detallado = {}
    
    for valor_upper in valores_upper:
        # Contar cuántas veces aparece ese valor específico
        conteo = (columna_upper == valor_upper).sum()
        if conteo > 0:
            # Almacenar el conteo usando el valor en MAYÚSCULAS como clave
            conteo_detallado[valor_upper] = conteo
            
    return conteo_detallado


def data_types(df, columnas_numericas):
    columnas_numericas = ['Quantity', 'Total Spent', 'Price Per Unit'] 
    df[columnas_numericas] = df[columnas_numericas].apply(
    pd.to_numeric, 
    errors='coerce' # Convierte cualquier cadena o error a np.nan
    )
    df[["Location", "Item", "Payment Method"]] = df[["Location", "Item", "Payment Method"]].astype(pd.StringDtype)
    df["Transaction Date"] = df["Transaction Date"]. apply(
    pd.to_datetime,
    errors='coerce'
)

def data_standarization(df):
    diccionario_items = {"Cake":3.0, "Coffee": 2.0,"Cookie": 1.0, "Juice": 3.0, "Salad": 5.0, "Sandwich": 4.0, "Smoothie": 4.0, "Tea":1.5 }
    print(diccionario_items)
    df["Price Per Unit"] = df["Item"].map(diccionario_items)
    return df








