import google.generativeai as genai
from core.config import AI_API_KEY

# Configurar la API de la IA
genai.configure(api_key=AI_API_KEY)

def analyze_sentiment(text: str):
    model = genai.GenerativeModel('gemini-3.1-flash-lite')
    try:
        response = model.generate_content(f"Analiza este comentario: '{text}'. Responde solo con una palabra: Positivo, Negativo o Neutro.")
        
        resultado = response.text.strip()
        print(f"DEBUG IA: {resultado}") 
        return resultado
    except Exception as e:
        print(f"Error real: {e}")
        return "Error en IA"