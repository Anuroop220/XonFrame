import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

genai.configure(api_key=api_key)

system_prompt = """You are ELIX, the voice assistant in XonFrame smart glasses.
Keep replies short and natural because they are read aloud. Use plain sentences, not lists.
Use the camera information when it helps in answering the user question."""

_model = genai.GenerativeModel(
    model_name="gemini-3.6-flash",
    system_instruction=system_prompt,
)


def ask_elix(user_input, detections=None):
    prompt = f"User said: {user_input}"
    if detections:
       prompt = f"I can see {', '.join(detections)}. {prompt}"

    try:
        response = _model.generate_content(prompt)
        return (response.text or "").strip() or "Sorry, I couldn't process that."
    except Exception:
        return "I couldn't reach the api now."