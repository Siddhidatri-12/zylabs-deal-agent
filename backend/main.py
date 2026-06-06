from fastapi import FastAPI
from pydantic import BaseModel

from backend.chat import chat
from backend.memory import (
    get_memories,
    delete_memory
)

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():

    return {
        "message": "Deal Intelligence Agent Running"
    }


@app.post("/chat")
def chat_endpoint(
    request: ChatRequest
):

    response = chat(
        request.message
    )

    return {
        "response": response
    }


@app.get("/memories")
def get_all_memories():

    return {
        "memories": get_memories()
    }


@app.delete("/memory/{value}")
def delete_memory_endpoint(
    value: str
):

    delete_memory(value)

    return {
        "status": "deleted",
        "value": value
    }
@app.get("/memory/search/{memory_type}")
def search_memory(memory_type: str):

    memories = get_memories()

    results = []

    for memory in memories:

        if memory[1] == memory_type:
            results.append(memory)

    return {
        "results": results
    }