# fastapi-image-upload-example

Ejemplo educativo con **FastAPI** para subir, validar y procesar imágenes de forma segura y asincrónica. Ideal para prácticas con modelos de Machine Learning, OCR o clasificación de imágenes.

# Propósito del proyecto

* **Backend para apps de visión por computadora**: Ideal como punto de partida para contruir APIs que integran modelos de detección de objetos (tal como esta simulación), OCR, clasificación de imagenes, incluso expandirlo a multimedia.

* **Procesamiento de imágenes/multimedia en proyectos de IA**: Ideal para probar pipelines de Machine Learning donde se sube una imagen y se obtienen predicciones desde un modelo o aplicar modelos de IA para transcribir, resumir audios o vídeos, etc.

* **Proyecto educativo para enseñar FastAPI**: Útil para explicar cómo trabajar con archivos, asincronía, validaciones y semáforos con FastAPI de forma clara y profesional. Puedes agregar más detalles, o robustecer más el código.

* **Testing de modelos en entornos controlados**: Permite enviar imágenes de prueba a un modelo (real o simulado) sin necesidad de interfaces gráficas.

* **Base para microservicio de ML**: Puede integrarse en arquitecturas de microservicios donde un servicio se encarga solo del análisis de imágenes (como en este ejemplo) o de cualquier otra función que determines.

* **Backend para apps móviles o frontends web**: Aplicaciones móviles o frontends en React/Vue pueden enviar imágenes al servidor para procesamiento o análisis.

* **Plantilla base para pruebas de stress/concurrencia**: Gracias al uso de Semaphore y asincronía, también es útil para probar cómo se comporta un servicio bajo múltiples solicitudes.

* **Automatización de cargas masivas de imágenes**: Sirve para proyectos donde se requiere procesar imágenes desde sistemas automatizados o scripts externos (como scrapers o pipelines de datos).

---

🚀 Características:
- Subida de archivos tipo imagen (PNG, JPEG)
- Validación segura usando la librería `filetype`
- Procesamiento simulado (ideal para integrar modelos ML/IA)
- Manejo de archivos temporales y concurrencia controlada con semáforo
- Asincronía eficiente usando `asyncio` y `run_in_executor`

💡 Ideal para aprender cómo construir un endpoint robusto en FastAPI para manejo de archivos multimedia

---

## 📂 Estructura del Proyecto

```bash
.
├── image_client_fastapi.py     # Script para enviar imágenes al endpoint (simula cliente)
├── image_endpoint_fastapi.py   # Servidor FastAPI con endpoint de procesamiento
├── tmp/                        # Directorio temporal para imágenes subidas (se crea solo)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

# ¿Cómo ejecutar?

1. Instala dependencias

```bash
pip install -r requirements.txt
```

2. Inicia el servidor

```bash
uvicorn image_endpoint_fastapi:app --reload
```
Esto inicia el servidor en http://localhost:8000 y recarga automáticamente si haces cambios (modo desarrollo).

3. Ejecutar el cliente (en otra terminal)
```bash
python image_client_fastapi.py
```


