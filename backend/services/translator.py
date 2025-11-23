import os
from openai import OpenAI
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_text_with_context(text: str, context: str) -> str:
    """
    Traduce el texto seleccionado. Intenta usar OpenAI primero, y si falla (cuota/error),
    usa Google Translate como respaldo gratuito.
    """
    # Intentar con OpenAI
    try:
        prompt = f"""
        Contexto: "{context}"
        Palabra/Frase a traducir: "{text}"
        
        Instrucciones:
        1. Traduce la "Palabra/Frase a traducir" al español.
        2. Usa el "Contexto" para determinar el significado correcto si es ambiguo.
        3. Devuelve SOLO la traducción, sin explicaciones adicionales.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un traductor experto y conciso."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.3
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ Error con OpenAI ({e}). Usando Google Translate como respaldo...")
        
        # Fallback: Google Translate
        try:
            translator = GoogleTranslator(source='auto', target='es')
            translation = translator.translate(text)
            # Limpiar la traducción (quitar puntos finales si existen)
            return translation.strip().rstrip('.')
        except Exception as e2:
            return f"[Error de traducción: {str(e2)}]"
