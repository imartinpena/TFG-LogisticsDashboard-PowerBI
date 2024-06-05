import pandas as pd
import sys
import os

def convert_csv_to_excel(csv_file_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Cargando el archivo CSV
        data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
        
        # Guardando el archivo como Excel
        output_file_path = os.path.join(output_directory, os.path.splitext(os.path.basename(csv_file_path))[0] + '.xlsx')
        data.to_excel(output_file_path, index=False)
        print(f'Archivo convertido exitosamente y guardado en: {output_file_path}')
    except Exception as e:
        print(f'Error al convertir el archivo: {e}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python script.py <ruta_al_archivo_CSV> <directorio_de_salida>")
    else:
        csv_file_path = sys.argv[1]
        output_directory = sys.argv[2]
        convert_csv_to_excel(csv_file_path, output_directory)