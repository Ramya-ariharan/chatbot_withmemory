import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_llm_response(chat_history):
    """
    chat_history = [
      {"role": "user", "content": "Hi"},
      {"role": "assistant", "content": "Hello"}
    ]
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # FAST + STABLE
        messages=chat_history,
        temperature=0.7
    )

    return response.choices[0].message.content
