import requests
import os

directorio_actual = os.getcwd()  # Obtiene el directorio actual

# Función para enviar una imagen a la API FastAPI
def enviar_imagen_a_api(ruta_imagen, modo="deteccion"):
    url = "http://localhost:8000/procesar-imagen/"
    archivos = {"imagen": open(ruta_imagen, "rb")}
    params = {"modo": modo}
    
    respuesta = requests.post(url, files=archivos, params=params)
    
    if respuesta.status_code == 200:
        print("Respuesta de la API:")
        print(respuesta.json())
    else:
        print(f"Error {respuesta.status_code}: {respuesta.text}")

if __name__ == "__main__":
    # Cambia aquí la ruta a la imagen que quieres enviar
    ruta = os.path.join(directorio_actual, "imagen_ejemplo.jpeg")
    enviar_imagen_a_api(ruta)
