from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import base64

app = FastAPI()

class GenerateRequest(BaseModel):
    genre: str
    mood: str
    tempo: int
    key: str
    scaleType: str
    durationSec: int
    instrument: str
    complexity: float

@app.get("/")
def root():
    return {"message": "D Music Generator Backend Running"}

@app.post("/api/generate")
async def generate_music(req: GenerateRequest):
    midi_bytes = b"MThd..."  # Placeholder
    return {
        "midi": base64.b64encode(midi_bytes).decode("ascii"),
        "meta": {"status": "success", "source": "demo"}
    }

@app.post("/api/remix")
async def remix_music(midi: UploadFile = File(...)):
    return {"midi": base64.b64encode(await midi.read()).decode("ascii")}

@app.post("/api/render")
async def render_audio(midi: UploadFile = File(...)):
    return {"message": "Rendering not implemented yet"}

@app.post("/api/save")
async def save_composition(midi: UploadFile = File(...)):
    return {"id": "demo-123"}
