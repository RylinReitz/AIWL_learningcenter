from fastapi import APIRouter
from pydantic import BaseModel
from ..services.llm_service import run_llm

router = APIRouter(prefix="/prompts", tags=["prompts"])

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 256

class PromptResponse(BaseModel):
    response: str

@router.post("/run", response_model=PromptResponse)
def run_prompt(req: PromptRequest):
    # This calls the llm service wrapper (placeholder)
    out = run_llm(req.prompt, max_tokens=req.max_tokens)
    return {"response": out}
