import os

class Config:
    LLM_MODEL_PATH = os.getenv("LLM_MODEL_PATH", "llm/models/default.gguf")
    LLM_SERVER_URL = os.getenv("LLM_SERVER_URL", "http://localhost:11434")  # example
