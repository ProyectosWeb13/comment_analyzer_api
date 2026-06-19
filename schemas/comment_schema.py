from pydantic import BaseModel
from typing import Optional

# Lo que envía el usuario para crear/actualizar
class CommentCreate(BaseModel):
    author: str
    content: str

# Lo que envía el usuario solo para analizar
class CommentAnalyze(BaseModel):
    content: str

# Lo que devuelve la API (ya con ID y sentimiento)
class CommentResponse(BaseModel):
    id: int
    author: str
    content: str
    sentiment: Optional[str] = None