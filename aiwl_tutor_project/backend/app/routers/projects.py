from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/projects", tags=["projects"])

class Project(BaseModel):
    id: str
    title: str
    description: str

_PROJECTS = [
    Project(id="storybot", title="StoryBot", description="Build a chatbot that writes short stories.").dict()
]

@router.get("/", response_model=List[Project])
def list_projects():
    return _PROJECTS
