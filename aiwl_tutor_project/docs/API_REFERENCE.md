# API Reference (Starter)

## Health
- `GET /api/health/` — returns service health.

## Lessons
- `GET /api/lessons/` — list available lessons.
- `GET /api/lessons/{lesson_id}` — get a single lesson.

## Prompts
- `POST /api/prompts/run` — run a prompt against the LLM.
  Request body: `{ "prompt": "text", "max_tokens": 256 }`
  Response body: `{ "response": "text" }`

## Projects
- `GET /api/projects/` — list mini-projects.
