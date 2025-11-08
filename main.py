# pipeline_runner.py
from Pipeline.Extraction import extract_data
import Pipeline.Transformations as T
from Pipeline.Validation import check_for_nulls
from IPython.display import display

RUTA_DATOS = 'data/dirty_cafe_sales.csv'

def main_pipeline():
    """Define y ejecuta la secuencia ETL."""
    
    # 1. EXTRAER
    df_raw = extract_data(RUTA_DATOS)
    if df_raw.empty:
        print("Pipeline detenido por error de extracción.")
        return

    # 2. PERFILAR (Opcional, pero útil para verificar el punto de partida)
    # Aquí puedes llamar a tu matriz de frecuencia si quieres registrar los errores iniciales.
    
    # 3. TRANSFORMAR
    df_clean = T.clean_na_values(df_raw.copy()) # Usar .copy() para seguridad
    df_clean = T.drop_duplicaciones(df_clean)

    # 4. VERIFICAR (Mostrar el resultado final de la limpieza)
    print("\n--- Resultados de la Limpieza ---")
    display(df_clean.head())
    display(df_clean.dtypes)

    print(check_for_nulls(df_clean))
    
    # 5. CARGAR (Aquí iría la lógica para guardar el CSV limpio o cargar a una DB)
    df_clean.to_csv('data/cleaned_cafe_sales.csv', index=False)
    print("Pipeline de limpieza finalizado con éxito.")

    
if __name__ == "__main__":
    main_pipeline()