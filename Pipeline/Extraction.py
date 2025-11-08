# cafe_pipeline/extraction.py
import pandas as pd

def extract_data(ruta_archivo: str) -> pd.DataFrame:
    """Extrae datos de un CSV con manejo de errores."""
    try:
        df = pd.read_csv(ruta_archivo)
        print(f"✅ Extracción exitosa desde: {ruta_archivo}")
        return df
    except FileNotFoundError:
        print(f"❌ ERROR: Archivo no encontrado en: {ruta_archivo}")
        return pd.DataFrame()