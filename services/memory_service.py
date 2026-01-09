import json
from services.redis_client import redis_client

MAX_MESSAGES = 10

def get_memory(session_id: str):
    data = redis_client.get(session_id)
    return json.loads(data) if data else []

def save_memory(session_id: str, history: list):
    redis_client.set(
        session_id,
        json.dumps(history),
        ex=3600
    )

def trim_memory(history: list):
    if len(history) > MAX_MESSAGES:
        return history[-MAX_MESSAGES:]
    return history
