# Contract Intelligence Copilot

LLM-powered assistant for legal contract clause analysis and risk detection.

## Features
- PDF parsing with `unstructured`
- Chunk-level LLM analysis
- Frontend via Streamlit (dark mode)
- Backend API via FastAPI

## Setup

```bash
git clone https://github.com/yourusername/contract-copilot.git
cd contract-copilot
pip install -r requirements.txt
```

Run backend:
```bash
cd backend
uvicorn main:app --reload
```

Run frontend:
```bash
cd frontend
streamlit run app.py
```