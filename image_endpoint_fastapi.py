import os
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from uuid import uuid4
import asyncio
import filetype
import time

app = FastAPI()

# Definimos el directorio donde se guardarán los archivos temporales
directorio_tmp = os.path.join(os.getcwd(), "tmp")
os.makedirs(directorio_tmp, exist_ok=True)  # Crea el directorio si no existe

# Semáforo para limitar la cantidad de tareas concurrentes. Para este ejemplo, limitamos a 2.
semaforo = asyncio.Semaphore(2)

# Simulamos un procesamiento de imagen (detección, clasificación, OCR, etc.)
def procesar_imagen(path: str) -> dict:
    # Aquí iría la lógica real con tu modelo de ML
    if os.path.exists(path):
        time.sleep(2)  # Simulamos un tiempo de procesamiento
        os.remove(path)  # Eliminamos el archivo temporal después del procesamiento

    # Simulamos una respuesta de modelo
    return {
        "status": "ok",
        "mensaje": "Procesamiento exitoso",
        "elementos_detectados": ["persona", "bicicleta", "perro"]
    }

# Endpoint para subir una imagen y procesarla según el modo solicitado
@app.post("/procesar-imagen/")
async def procesar_imagen_endpoint(
    imagen: UploadFile = File(...),  # Archivo que se sube
    modo: str = Query("deteccion", enum=["deteccion", "clasificacion", "ocr"])  # Modo de análisis
):
    # Validamos que el archivo tenga un nombre (es decir, fue enviado)
    if not imagen.filename:
        raise HTTPException(status_code=400, detail="No se ha proporcionado un archivo.")

    # Leemos el contenido del archivo para inspeccionarlo
    contenido = await imagen.read()

    # Detectamos el tipo de archivo a partir del contenido
    tipo = filetype.guess_mime(contenido)

    # Solo aceptamos imágenes JPEG y PNG
    if tipo not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Solo se permiten imágenes JPEG o PNG.")

    # Construimos una ruta de archivo temporal única
    extension = imagen.filename.split(".")[-1]
    temp_path = os.path.join(directorio_tmp, f"{uuid4()}.{extension}")

    # Guardamos el contenido en un archivo temporal para procesarlo
    with open(temp_path, "wb") as buffer:
        buffer.write(contenido)

    # Ejecutamos el procesamiento de forma asíncrona, controlando concurrencia con semáforo
    async with semaforo:
        # Ejecutamos el procesamiento en un hilo aparte para no bloquear el event loop
        loop = asyncio.get_event_loop()
        # `run_in_executor(None, func, arg)` usa el ThreadPoolExecutor por defecto (None)
        # Ideal para funciones que hacen I/O o son bloqueantes (como procesar_imagen)
        resultado = await loop.run_in_executor(None, procesar_imagen, temp_path)

    # Respondemos con el resultado y el modo seleccionado
    return JSONResponse(content={
        "modo": modo,
        "resultado": resultado
    })
