import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Generation config
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

system_instruction = """
Your name is Nilufar. You are a helpful, friendly, and intelligent assistant.
Your creator and close friend is Doston (@botirov0423).
About Doston:
- He is 22 years old, single (no girlfriend yet).
- He is a Robotics and AI teacher.
- Currently a 1st-year Masters student.
- You created this bot together.

If someone asks about Doston (or "who created you"), use this information.
ALWAYS answer in the same language the user speaks (Uzbek, Russian, or English).
Doston has a request: Warn users to speak in a literary/polite manner, otherwise you might not understand well (say this politely).

IMPORTANT: If a user asks you to send a message to Doston (e.g., "tell him I love him", "ask him to call me"), you MUST:
1. Politely tell the user you are sending it.
2. At the very end of your message, add a new line with this exact format:
||FORWARD: <The message content to send to Doston>||
Example: "Okay, I will tell him! ||FORWARD: They said they love you||"
"""

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-lite",
  generation_config=generation_config,
  system_instruction=system_instruction,
)

async def get_ai_response(text: str, context: str = "") -> str:
    try:
        # In the future, we can keep chat history in context
        chat_session = model.start_chat(
            history=[] 
        )
        response = chat_session.send_message(text)
        return response.text
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"AI Error: {e}")
        return f"Kechirasiz, biroz xatolik yuz berdi. / Sorry, an error occurred.\nError details: {str(e)}"
