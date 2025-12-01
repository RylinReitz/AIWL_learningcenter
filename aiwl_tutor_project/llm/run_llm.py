"""Lightweight wrapper script that would run or proxy to a local model.
Replace the body of `generate` with integration to llama.cpp, ctranslate2, ollama, or another runtime.
"""
import argparse

def generate(prompt: str, max_tokens: int = 256) -> str:
    # TODO: integrate with local model runtime
    return f"[mock-llm] Generated for prompt: {prompt[:200]}{'...' if len(prompt)>200 else ''}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, default="Hello")
    parser.add_argument('--max-tokens', type=int, default=256)
    args = parser.parse_args()
    print(generate(args.prompt, args.max_tokens))
