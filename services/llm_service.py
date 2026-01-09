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



SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a helpful AI assistant. "
        "You remember user context within the conversation. "
        "Be concise, clear, and professional."
    )
}

def get_llm_response_memory(chat_history):
    messages = [SYSTEM_PROMPT] + chat_history

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content