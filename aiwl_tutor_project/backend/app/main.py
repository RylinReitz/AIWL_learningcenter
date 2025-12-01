from fastapi import FastAPI
from .routers import health, lessons, prompts, projects

app = FastAPI(title="AIWL Tutor Backend")

app.include_router(health.router)
app.include_router(lessons.router)
app.include_router(prompts.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "AIWL backend running"}
