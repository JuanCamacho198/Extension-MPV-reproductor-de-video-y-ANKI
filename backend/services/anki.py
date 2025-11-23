import requests
import os
from dotenv import load_dotenv

load_dotenv()

ANKI_CONNECT_URL = "http://localhost:8765"
DECK_NAME = os.getenv("ANKI_DECK", "Default")
MODEL_NAME = os.getenv("ANKI_MODEL", "Basic")

def add_card(front: str, back: str, context: str = "") -> dict:
    """
    Añade una nota a Anki usando AnkiConnect.
    """
    # Limpiar el texto frontal (quitar puntos finales y espacios extra)
    clean_front = front.strip().rstrip('.')
    
    # Formatear el reverso
    # El usuario pidió SOLO la traducción, sin el contexto del subtítulo.
    final_back = back
    
    # Si en el futuro queremos añadir ejemplos generados por IA, se harían aquí.
    # Por ahora, mantenemos el reverso limpio solo con la traducción.

    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": DECK_NAME,
                "modelName": MODEL_NAME,
                "fields": {
                    "Front": clean_front,
                    "Back": final_back
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": ["mpv-anki"]
            }
        }
    }

    try:
        print(f"Intentando añadir tarjeta al mazo: '{DECK_NAME}' con modelo: '{MODEL_NAME}'")
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        result = response.json()
        
        if result.get("error"):
            return {"status": "error", "message": result["error"]}
            
        return {"status": "success", "cardId": result["result"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
