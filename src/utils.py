import subprocess

def call_llm(prompt):
    """Call Ollama LLM (Mistral) and return a response."""
    result = subprocess.run(["ollama", "run", "mistral", prompt], capture_output=True, text=True)
    return result.stdout.strip()
