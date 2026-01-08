import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

from app.schemas import NoteInput, QAAnalysisResponse
from app.services.google_service import GoogleQAProvider

app = FastAPI(title="FirstImpact Med Clinical QA Engine")
provider = GoogleQAProvider()

@app.get("/")
def health():
    return {"status": "active", "engine": "Gemini-2.0-Flash"}

@app.post("/analyze-note", response_model=QAAnalysisResponse)
async def analyze_note(payload: NoteInput):
    try:
        return await provider.analyze(payload.model_dump())
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))