import pandas as pd
import json
import os

def procesar_datos(json_file='data.json', excel_file='output.xlsx'):
    if not os.path.exists(json_file):
        print(f"Error: El archivo '{json_file}' no existe.")
        return

    try:
        # Leer el archivo JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Verificar que sea una lista de diccionarios
        if isinstance(data, dict):
            data = [data]  # Convertir en lista si es un solo diccionario
        
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            print("Error: El JSON debe contener una lista de diccionarios.")
            return
        
        # Crear DataFrame y guardar en Excel
        df = pd.json_normalize(data)  # Normaliza estructuras anidadas si es necesario
        df.to_excel(excel_file, index=False)
        print(f"Archivo Excel '{excel_file}' generado exitosamente.")
    
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato inválido.")
    except Exception as e:
        print(f"Error al procesar datos: {e}")

if __name__ == '__main__':
    procesar_datos()
