import requests
import json

def test_anki_connection():
    url = "http://localhost:8765"
    payload = {
        "action": "version",
        "version": 6
    }

    try:
        print(f"Intentando conectar a {url}...")
        response = requests.post(url, json=payload)
        data = response.json()
        
        if 'result' in data:
            print(f"✅ ¡Conexión exitosa! Versión de AnkiConnect: {data['result']}")
            
            # Verificar Mazo y Modelo
            deck_payload = {"action": "deckNames", "version": 6}
            model_payload = {"action": "modelNames", "version": 6}
            
            decks = requests.post(url, json=deck_payload).json()['result']
            models = requests.post(url, json=model_payload).json()['result']
            
            print("\nMazos disponibles:", decks)
            print("Tipos de nota disponibles:", models)
            
            print("\nRecuerda actualizar tu archivo .env si tus nombres son diferentes (ej. 'Básico' vs 'Basic').")
        else:
            print("❌ Conexión establecida pero respuesta inesperada:", data)
            
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar a Anki.")
        print("Asegúrate de que:")
        print("1. Anki está abierto.")
        print("2. AnkiConnect está instalado.")
        print("3. Has reiniciado Anki después de instalar el complemento.")

if __name__ == "__main__":
    test_anki_connection()
