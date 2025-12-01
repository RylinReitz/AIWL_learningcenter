# AI World Leaders — Tutor (Starter Project)

This repository is a starter template for a local-first tutoring website that helps teach students to use AI tools.

## Structure
- `backend/` — FastAPI backend (API + LLM proxy)
- `frontend/` — Static frontend files (public/)
- `llm/` — Local model wrapper and models folder
- `docs/` — Architecture, API, lesson plan guide

## Run (development)
1. Python backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
2. Static frontend:
   Serve `frontend/public` with any static server (or use the Docker compose included).

## Notes
- This is a starter scaffold. The LLM integration is mocked and must be wired to a real runtime.
