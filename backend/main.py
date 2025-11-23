from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="MPV Anki Bridge")

# Configurar CORS para permitir peticiones desde el frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class SubtitlePayload(BaseModel):
    text: str
    timestamp: Optional[float] = None
    filename: Optional[str] = None

class TranslationRequest(BaseModel):
    text: str
    context: str

class AnkiCard(BaseModel):
    front: str
    back: str
    context: str

# Estado global (en memoria)
current_subtitle: Optional[SubtitlePayload] = None

@app.get("/")
def read_root():
    return {"status": "ok", "message": "MPV Anki Bridge Backend is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/capture")
def capture_subtitle(payload: SubtitlePayload):
    global current_subtitle
    current_subtitle = payload
    print(f"Subtítulo capturado: {payload.text}")
    return {"status": "captured", "data": payload}

@app.get("/api/current-subtitle")
def get_current_subtitle():
    return current_subtitle if current_subtitle else {"text": "", "timestamp": 0}

@app.post("/api/translate")
def translate_text(request: TranslationRequest):
    # TODO: Implementar llamada a OpenAI/DeepL
    # Mock response por ahora
    return {"original": request.text, "translation": f"[Traducción de: {request.text}]"}

@app.post("/api/anki/add")
def add_to_anki(card: AnkiCard):
    # TODO: Implementar llamada a AnkiConnect
    print(f"Añadiendo a Anki: {card.front} -> {card.back}")
    return {"status": "success", "cardId": 12345}
