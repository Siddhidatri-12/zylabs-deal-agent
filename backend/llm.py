import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(question, context):

    prompt = f"""
You are an AI Deal Intelligence Agent.

Use BOTH:

1. Stored memories
2. Retrieved knowledge base context

to answer the user's question.

If memory contains the answer,
prioritize memory.

Context:

{context}

Question:

{question}

Answer:
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        print("\nLLM ERROR:")
        print(e)

        return (
            "AI service temporarily unavailable. "
            "Please try again later."
        )