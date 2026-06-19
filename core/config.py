import os
from dotenv import load_dotenv

# Cargar las variables del .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
AI_API_KEY = os.getenv("AI_API_KEY")