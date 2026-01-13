# llm.py
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"

def get_llm_response(system_prompt, user_prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        r.raise_for_status()
        return r.json()["message"]["content"]
    except Exception:
        return "⚠️ Unable to connect to local LLM. Please ensure Ollama is running."
