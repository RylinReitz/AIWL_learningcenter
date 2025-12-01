# Architecture Overview

This project is designed as a local-first tutoring website for AI World Leaders.

Components:
- **Frontend**: Static site (public/) served either by a static server or via the backend.
- **Backend**: FastAPI service that exposes endpoints for lessons, prompts and projects.
  It also acts as a proxy to a local LLM runtime.
- **LLM**: Local model runtime (llama.cpp, ollama, or a dedicated inference server).
- **Docker**: Optional docker-compose for local development.

Communication:
- Frontend -> Backend: HTTP API under /api/*
- Backend -> LLM: local process or HTTP on localhost
