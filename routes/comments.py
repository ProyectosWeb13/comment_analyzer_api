from fastapi import APIRouter, HTTPException
from database.supabase import supabase
from schemas.comment_schema import CommentCreate, CommentAnalyze
from services.ai_service import analyze_sentiment

router = APIRouter(prefix="/comments", tags=["Comments"])

# 1. GET /comments - Listar todos
@router.get("/")
def get_comments():
    response = supabase.table('comments').select('*').execute()
    return response.data

# 2. GET /comments/{id} - Obtener uno por ID
@router.get("/{id}")
def get_comment(id: int):
    response = supabase.table('comments').select('*').eq('id', id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Comentario no encontrado bro")
    return response.data[0]

# 3. POST /comments - Crear comentario (con IA automática)
@router.post("/")
def create_comment(comment: CommentCreate):
    # Validar que no vengan vacíos como pide la prueba inválida del profe
    if not comment.author.strip() or not comment.content.strip():
        raise HTTPException(status_code=400, detail="Los campos author y content son obligatorios")

    # Sacar el sentimiento con la IA antes de guardar
    sentiment = analyze_sentiment(comment.content)
    
    # Guardar en la BD
    new_comment = {
        "author": comment.author,
        "content": comment.content,
        "sentiment": sentiment
    }
    response = supabase.table('comments').insert(new_comment).execute()
    return response.data[0]

# 4. PUT /comments/{id} - Actualizar
@router.put("/{id}")
def update_comment(id: int, comment: CommentCreate):
    # Si cambia el contenido, volvemos a analizar el sentimiento
    sentiment = analyze_sentiment(comment.content)
    
    updated_data = {
        "author": comment.author,
        "content": comment.content,
        "sentiment": sentiment
    }
    
    response = supabase.table('comments').update(updated_data).eq('id', id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Comentario no encontrado para actualizar")
    return response.data[0]

# 5. DELETE /comments/{id} - Eliminar
@router.delete("/{id}")
def delete_comment(id: int):
    response = supabase.table('comments').delete().eq('id', id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Ese ID no existe")
    return {"mensaje": "Comentario borrado con éxito"}

# 6. POST /comments/analyze - Solo usar la IA sin guardar
@router.post("/analyze")
def analyze_only(data: CommentAnalyze):
    sentiment = analyze_sentiment(data.content)
    return {
        "content": data.content,
        "sentiment": sentiment
    }