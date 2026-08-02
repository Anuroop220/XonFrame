import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

SYSTEM_PROMPT = """You are E.L.I.X, an AI assistant built into smart glasses called XonFrame.
You are helpful, concise and smart. You can see what the user sees through a camera.
Keep responses short and natural — you are speaking out loud through bone conduction speakers.
Never use bullet points or lists. Always respond in plain conversational sentences."""

def ask_elix(user_input, detections=None):
    context = ""
    if detections:
        context = f"I can currently see: {', '.join(detections)}. "
    
    prompt = f"{context}User said: {user_input}"
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        data = response.json()
        return data.get("response", "Sorry, I couldn't process that.")
    except Exception as e:
        return "I'm having trouble connecting to my brain right now."