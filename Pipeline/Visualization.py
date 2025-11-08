# cafe_pipeline/visualization.py

import matplotlib.pyplot as plt
import pandas as pd

def plot_transacciones_mensuales(df: pd.Series):
    """
    Genera y muestra una gráfica de barras del número de transacciones por mes.

    Args:
        conteo_mensual (pd.Series): Serie con el índice como Mes_Año (str) 
                                    y los valores como el conteo de transacciones.
    """
    
    COLUMNA_FECHA = 'Transaction Date' 

    df['Mes_Año'] = df[COLUMNA_FECHA].dt.to_period('M')
    conteo_mensual = df.groupby('Mes_Año').size()
    conteo_mensual.index = conteo_mensual.index.astype(str)

    plt.figure(figsize=(12, 6)) # Define el tamaño de la gráfica
    plt.bar(
        conteo_mensual.index,    # Eje X: Los meses (ej. '2024-01', '2024-02')
        conteo_mensual.values,   # Eje Y: El número de transacciones
        color='skyblue'
    )

    # Añadir etiquetas y títulos
    plt.title('Número de Transacciones por Mes y Año')
    plt.xlabel('Mes y Año')
    plt.ylabel('Total de Transacciones')

    # Rotar las etiquetas del eje X para evitar que se superpongan
    plt.xticks(rotation=45, ha='right')

    # Añadir una cuadrícula para facilitar la lectura
    plt.grid(axis='y', linestyle='--')

    # Ajustar los márgenes para que todo quepa
    plt.tight_layout() 

    # Mostrar la gráfica
    plt.show()