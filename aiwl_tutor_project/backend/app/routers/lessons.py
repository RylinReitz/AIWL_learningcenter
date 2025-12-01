from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/lessons", tags=["lessons"])

class Lesson(BaseModel):
    id: str
    title: str
    duration_minutes: int
    content: str

# In-memory placeholder store
_LESSONS = [
    Lesson(id="intro-ai", title="Intro to AI", duration_minutes=10, content="What is AI...").dict()
]

@router.get("/", response_model=List[Lesson])
def list_lessons():
    return _LESSONS

@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: str):
    for l in _LESSONS:
        if l["id"] == lesson_id:
            return l
    return {"id": "not-found", "title": "Not Found", "duration_minutes": 0, "content": ""}
