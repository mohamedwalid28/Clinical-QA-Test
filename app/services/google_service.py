import os
from google import genai
from app.schemas import QAAnalysisResponse

class GoogleQAProvider:
    def __init__(self):
        # Initialize the 2026 SDK Client
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # USE THE LEGACY STABLE ALIAS: This has the highest chance of a non-zero free limit
        self.model_id = "gemini-flash-latest" 

    async def analyze(self, data: dict):
        instructions = (
            """
            You are an expert Clinical Quality Assurance Auditor. Your task is to review clinical notes for defensibility, accuracy, and professional tone.

            CORE CLINICAL RULES:
            1. NO FABRICATION: Do not invent clinical findings not present in the note.
            2. MINIMAL EDITS: Suggested edits must be concise and improve defensibility without rewriting the whole note.
            3. GAP IDENTIFICATION: If key information is missing (dates, specific exam findings), flag it as missing.
            4. NEUTRALITY: Ensure language is neutral. Replace subjective clinician bias (e.g., "patient is lazy") with objective observations (e.g., "patient's self-reported activity level is low").
            5. SEPARATION: Maintain clear distinction between patient-reported history (Subjective) and clinician findings (Objective).

            SCORING CRITERIA:
            - 90-100 (A+): Defensible, objective, complete.
            - 80-89 (A/B): Minor documentation gaps.
            - 70-79 (C): Major issues, biased language, or missing critical sections.
            - <70 (D): Critical errors or high legal risk.
            """
        )
        
        prompt = f"Note Content: {data['note']}"

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config={
                    "system_instruction": instructions,
                    "response_mime_type": "application/json",
                    "response_schema": QAAnalysisResponse,
                }
            )
            return response.parsed
            
        except Exception as e:
            # If still limit 0, provide the professional explanation
            if "429" in str(e) and "limit: 0" in str(e):
                print("\n❌ CRITICAL: Your Google AI Studio account has a hard limit of 0.")
                print("FIX: Go to https://aistudio.google.com/app/settings")
                print("ENABLE: 'Pay-as-you-go' (It is $0/free, but required for verification).\n")
            raise e