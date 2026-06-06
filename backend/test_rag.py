# backend/test_rag.py

from backend.rag import retrieve_context
from backend.llm import generate_answer

query = "What are strong buying signals?"

context = retrieve_context(query)

answer = generate_answer(
    query,
    context
)

print(answer)