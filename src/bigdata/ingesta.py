import requests
import json

def obtener_datos_api(url):
    try:
        response = requests.get(url, verify=False)  # Deshabilita SSL
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
        return {}

url = "https://dragonball-api.com/api/characters"
datos = obtener_datos_api(url)

if datos:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("Datos guardados en 'data.json'")
else:
    print("No se obtuvo respuesta válida de la API")
