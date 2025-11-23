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
    # Formatear el reverso para incluir el contexto si existe
    final_back = back
    if context:
        final_back += f"<br><br><small><i>Contexto: {context}</i></small>"

    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": DECK_NAME,
                "modelName": MODEL_NAME,
                "fields": {
                    "Front": front,
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
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        result = response.json()
        
        if result.get("error"):
            return {"status": "error", "message": result["error"]}
            
        return {"status": "success", "cardId": result["result"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
