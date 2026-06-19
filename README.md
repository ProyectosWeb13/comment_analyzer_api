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
*(Aquí irán tus capturas)*
- **Prueba Válida 1:** ![Prueba Válida 1](docs/screenshots/test-valid-1.png)
- **Prueba Válida 2 (IA):** ![Prueba Válida 2](docs/screenshots/test-valid-2.png)
- **Prueba Inválida:** ![Prueba Inválida](docs/screenshots/test-invalid-1.png)

## 🎥 Video de Funcionamiento
El video detallando el funcionamiento completo de la API se encuentra disponible en:
[PEGA AQUÍ TU ENLACE DEL VIDEO]

## 📊 Evidencia de Base de Datos (Supabase)
![Tabla en Supabase](docs/screenshots/supabase-table.png)

## ⚙️ Tecnologías Utilizadas
- **Framework:** FastAPI
- **Base de Datos:** Supabase (PostgreSQL)
- **IA:** Google Gemini API (Modelo: gemini-3-flash-preview)
- **Lenguaje:** Python 3.x