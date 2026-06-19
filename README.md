# API de Análisis de Comentarios - Proyecto Final Web II

👥 Integrantes del Proyecto
Guillermo Gonzalez Mattos
Andres Jimenes
Andres Felipe

API REST desarrollada con **FastAPI**, **Supabase** y **Google Gemini AI** para el análisis de sentimiento en comentarios.

## 🚀 Estructura del Proyecto
```text
project/
├── docs/screenshots/     # Capturas de las pruebas
├── core/                 # Configuración de variables de entorno
├── database/             # Conexión a Supabase
├── routes/               # Endpoints de la API (CRUD y IA)
├── schemas/              # Modelos de datos (Pydantic)
├── services/             # Lógica de la IA
├── main.py               # Punto de entrada
└── .env.example          # Plantilla de variables de entorno


## 🧪 Pruebas de la API
[Prueba Válida 1](docs/screenshots/test-valid-1.png)
[Prueba Válida 2 (IA)](docs/screenshots/test-valid-2.png)
[Prueba Inválida](docs/screenshots/test-invalid-1.png)



## 🎥 Video de Funcionamiento
El video detallando el funcionamiento completo de la API se encuentra disponible en:
https://drive.google.com/drive/folders/1UqMxQcD2ESrvMbCku8purapCE7W40jri?usp=sharing

## 📊 Evidencia de Base de Datos (Supabase)
[Tabla en Supabase](docs/screenshots/supabase-table.png)

## ⚙️ Tecnologías Utilizadas
- **Framework:** FastAPI
- **Base de Datos:** Supabase (PostgreSQL)
- **IA:** Google Gemini API (Modelo: gemini-3-flash-lite)
- **Lenguaje:** Python 3.x

## 🛠️ Instalación y Ejecución

1. Clona el repositorio:
   `git clone https://github.com/TU_USUARIO/TU_REPO.git`

2. Crea un entorno virtual e instala las dependencias:
   `python -m venv venv`
   `pip install -r requirements.txt`

3. Crea un archivo `.env` basado en `.env.example` con tus credenciales de Supabase y tu API KEY de Gemini.

4. Ejecuta el servidor:
   `uvicorn main:app --reload`


Arquitectura de Procesamiento:
Cada comentario recibido pasa por un servicio de análisis que utiliza gemini-1.5-flash. El resultado del análisis (Positivo, Negativo o Neutral) se almacena junto al contenido original en la base de datos de Supabase.