from fastapi import APIRouter
from schemas.chat_schemas import ChatRequest, ChatResponse
from services.memory_service import get_chat_history, save_message
from services.llm_service import get_llm_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    session_id = request.session_id
    user_message = request.message

    # 1️⃣ Save user message
    save_message(session_id, "user", user_message)

    # 2️⃣ Get full conversation
    chat_history = get_chat_history(session_id)

    # 3️⃣ Call LLM with memory
    bot_reply = get_llm_response(chat_history)

    # 4️⃣ Save bot reply
    save_message(session_id, "assistant", bot_reply)

    return ChatResponse(response=bot_reply)
