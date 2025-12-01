from pydantic import BaseModel

class LLMRequest(BaseModel):
    prompt: str
    max_tokens: int = 256

class LLMResponse(BaseModel):
    text: str
