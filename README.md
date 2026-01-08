# 🩺 Clinical QA Engine: Intelligence Core
### **Next-Gen Clinical Note Defensibility & Audit Automation**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlegemini)](https://ai.google.dev/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic)](https://docs.pydantic.dev/)

The **Clinical QA Engine** is a high-performance backend service built to transform raw clinical documentation into structured, defensible medical records. Utilizing the **Gemini 2.0/3.0 Flash** reasoning core, the engine performs real-time auditing against internal QA standards to identify risks, enforce neutral language, and suggest minimal, high-impact edits.

---

## 🚀 The Brain: System Architecture

The engine is engineered with a **Provider-Service Pattern**, decoupling the AI's reasoning from the API's infrastructure.

| Component | Responsibility |
| :--- | :--- |
| **FastAPI Gateway** | High-throughput async endpoint handling and OpenAPI/Swagger documentation. |
| **Pydantic Validation** | Strict schema enforcement. If the AI doesn't follow the "Clinical Contract," the data is rejected. |
| **Google GenAI (v2)** | Advanced reasoning core using **Schema-Guided Generation** for 100% parseable JSON. |
| **Clinical Logic Core** | Injects FirstImpact Med’s non-negotiable rules (Neutrality, Fact-Retention, Gap Analysis). |

---

## 🛠️ Quick Start: Deploying the Engine

### 1. Environment Synthesis
Clone the repo and initialize your 2026 Python environment:
```cmd
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn[standard] google-genai python-dotenv pydantic
```

### 2. Secure Configuration
Create a `.env` file in the root directory. This keeps your credentials out of source control.
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Ignition
Launch the service with hot-reloading:
```cmd
python -m uvicorn app.main:app --reload
```
> **Access the Console:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the professional Swagger UI.

---

## 🧠 Clinical IQ: Non-Negotiable Rules

The AI is hard-coded via **System Instructions** to follow these FirstImpact Med standards:

1.  **Zero Fabrication:** The engine is prohibited from inventing clinical findings.
2.  **Minimal Edits:** We don't rewrite the note; we surgically refine it for defensibility.
3.  **Gap Detection:** Missing dates or findings are flagged as "Critical" or "Major" risks.
4.  **Neutral Language:** The engine strips clinician bias (e.g., converting *"Patient is exaggerating"* to *"Symptoms reported appear out of proportion to clinical findings"*).
5.  **Audit Integrity:** Every response contains exactly **3–5 QA flags**.

---

## 📡 API Specification

### `POST /analyze-note`

**Input Payload:**
```json
{
  "note": "Patient is lazy and won't do exercises. Claims back hurts. I think they are faking it.",
  "note_type": "Progress Note",
  "date_of_service": "2026-01-08",
  "date_of_injury": "2025-12-15"
}
```

**Intelligence Output:**
```json
{
  "overall_score": 72,
  "letter_grade": "C",
  "flags": [
    {
      "severity": "critical",
      "issue": "Use of subjective, biased language ('lazy', 'faking it').",
      "suggested_edit": "Patient reports limited adherence to exercise protocol; clinical findings do not fully correlate with subjective pain levels."
    },
    {
      "severity": "major",
      "issue": "Missing objective range-of-motion measurements.",
      "suggested_edit": "Include specific degrees of lumbar flexion and extension."
    },
    {
      "severity": "minor",
      "issue": "Note lacks separation of subjective and objective sections.",
      "suggested_edit": "Organize findings under distinct 'History' and 'Physical Exam' headers."
    }
  ]
}
```

---

## ⚖️ Trade-offs & Decisions

*   **Model Selection:** We prioritized **Gemini 2.0 Flash-Lite** for the production environment to balance high-reasoning capabilities with 2026's optimized free-tier quotas.
*   **Schema Enforcement:** We utilized the 2026 `google-genai` SDK's native `response_schema`. This eliminates the need for manual JSON parsing and prevents common "hallucination" errors where the AI returns lists instead of objects.
*   **Asynchronous Processing:** The API is built on `async/await` to ensure that while the AI is thinking, the server can still accept other incoming clinical requests without blocking.

---

## 📈 Future Roadmap

1.  **Multi-Model Fallback:** Implement an automated switch to **Anthropic Claude** or **Local Llama 4** if the Google quota is exhausted.
2.  **HIPAA-Compliant Logging:** Integration with secure audit trails to track how QA scores improve clinician documentation over time.
3.  **Note Comparison:** A secondary endpoint to compare the original note vs. the suggested edits to calculate a "Defensibility Lift Score."

---

**Developed for FirstImpact Med Technical Test — January 2026**  
*Turning clinical narratives into defensible data.*