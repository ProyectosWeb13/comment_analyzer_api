# API de Análisis de Comentarios - Proyecto Final Web II

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
https://github.com/ProyectosWeb13/comment_analyzer_api/raw/main/docs/screenshots/test-invalid-1.PNG

## 🎥 Video de Funcionamiento
El video detallando el funcionamiento completo de la API se encuentra disponible en:
https://drive.google.com/drive/folders/1UqMxQcD2ESrvMbCku8purapCE7W40jri?usp=sharing

## 📊 Evidencia de Base de Datos (Supabase)
![Tabla en Supabase](docs/screenshots/supabase-table.png)

## ⚙️ Tecnologías Utilizadas
- **Framework:** FastAPI
- **Base de Datos:** Supabase (PostgreSQL)
- **IA:** Google Gemini API (Modelo: gemini-3-flash-preview)
- **Lenguaje:** Python 3.x