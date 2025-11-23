import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_text_with_context(text: str, context: str) -> str:
    """
    Traduce el texto seleccionado teniendo en cuenta el contexto (la frase completa).
    """
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
        print(f"Error en traducción: {e}")
        return f"[Error: {str(e)}]"
