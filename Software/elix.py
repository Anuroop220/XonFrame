"""
elix.py — E.L.I.X's "brain": takes a user utterance + current object
detections and returns a spoken-friendly reply.

This used to call a local Ollama model (llama3.2). Since you're using a
laptop-hosted setup with a Gemini API key for this submission, it now calls
Gemini directly. Imported by main.py.

For the separate Flask server that lets the HTML console chat with E.L.I.X
over HTTP, see elix_bridge.py — that's a different entry point (run as its
own process) and is not used by main.py.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not set. Create a .env file next to elix.py with:\n"
        "GEMINI_API_KEY=your-key-here"
    )

genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """You are E.L.I.X, an AI assistant built into smart glasses called XonFrame.
You are helpful, concise and smart. You can see what the user sees through a camera.
Keep responses short and natural — you are speaking out loud through bone conduction speakers.
Never use bullet points or lists. Always respond in plain conversational sentences."""

_model = genai.GenerativeModel(model_name="gemini-2.0-flash", system_instruction=SYSTEM_PROMPT)


def ask_elix(user_input, detections=None):
    context = ""
    if detections:
        context = f"I can currently see: {', '.join(detections)}. "

    prompt = f"{context}User said: {user_input}"

    try:
        response = _model.generate_content(prompt)
        return (response.text or "").strip() or "Sorry, I couldn't process that."
    except Exception:
        return "I'm having trouble connecting to my brain right now."
