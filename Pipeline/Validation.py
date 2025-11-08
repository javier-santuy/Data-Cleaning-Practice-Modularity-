import pandas as pd

def check_for_nulls(df: pd.DataFrame) -> bool:
    """Verifica si hay valores nulos en alguna columna y reporta el total."""
    null_counts = df.isnull().sum()
    total_nulls = null_counts.sum()
    
    if total_nulls > 0:
        print(f"⚠️ Alerta de Calidad: Se encontraron {total_nulls} valores nulos.")
        # Opcional: print(null_counts[null_counts > 0])
        return False
    
    print("✅ Calidad: No se encontraron valores nulos.")
    return True