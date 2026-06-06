from ollama import chat


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

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print("\nLLM ERROR:")
        print(e)

        return (
            "AI service temporarily unavailable. "
            "Please try again later."
        )