from pydantic import BaseModel, Field
from typing import List, Literal

# Input for the API
class NoteInput(BaseModel):
    note: str
    note_type: str
    date_of_service: str
    date_of_injury: str

# Structure for each QA issue
class QAFlag(BaseModel):
    severity: Literal["critical", "major", "minor"]
    issue: str = Field(..., description="Why it matters")
    suggested_edit: str = Field(..., description="1-2 sentences max")

# Final structured output
class QAAnalysisResponse(BaseModel):
    overall_score: int = Field(..., description="Score from 0 to 100")
    letter_grade: Literal["A+", "A", "B", "C", "D"]
    flags: List[QAFlag]