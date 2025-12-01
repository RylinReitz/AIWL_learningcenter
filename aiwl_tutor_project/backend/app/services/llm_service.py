import os
from ..utils.config import Config

def run_llm(prompt: str, max_tokens: int = 256) -> str:
    """Placeholder LLM runner.
    Replace this implementation with a call to your local LLM server,
    llama.cpp wrapper, ollama, or an HTTP API to a model.
    """
    # For now return a deterministic mock response.
    return f"[mock-llm] Reply to: {prompt[:200]}{'...' if len(prompt)>200 else ''}"
