from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from services.translator import translate_text_with_context
from services.anki import add_card

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
    translation = translate_text_with_context(request.text, request.context)
    return {"original": request.text, "translation": translation}

@app.post("/api/anki/add")
def add_to_anki(card: AnkiCard):
    result = add_card(card.front, card.back, card.context)
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["message"])
    return result
