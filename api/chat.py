from fastapi import APIRouter
from schemas.chat_schemas import ChatRequest, ChatResponse

from services.llm_service import get_llm_response, get_llm_response_memory
from services.memory_service import get_memory, save_memory,trim_memory

router = APIRouter()





@router.post("/chat-with-memory", response_model=ChatResponse)
def chat(request: ChatRequest):
    session_id = request.session_id

    # 1️⃣ Get existing memory
    history = get_memory(session_id)

    # 2️⃣ Add user message
    history.append({
        "role": "user",
        "content": request.message
    })

    # 3️⃣ Call LLM with memory
    reply = get_llm_response_memory(history)

    # 4️⃣ Add assistant reply
    history.append({
        "role": "assistant",
        "content": reply
    })

    # 5️⃣ Trim memory (IMPORTANT 🔥)
    history = trim_memory(history)

    # 6️⃣ Save back to Redis
    save_memory(session_id, history)

    return ChatResponse(response=reply)
