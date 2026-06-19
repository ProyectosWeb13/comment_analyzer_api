from fastapi import FastAPI
from routes import comments

app = FastAPI(
    title="API de Comentarios con IA",
    description="Trabajo Final Web II - CRUD con Supabase e IA",
    version="1.0.0"
)

# Conectar las rutas
app.include_router(comments.router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}