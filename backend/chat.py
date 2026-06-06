from backend.rag import retrieve_context
from backend.llm import generate_answer

from backend.memory import (
    get_memory_context,
    save_or_update_memory,
    get_memories
)

from backend.memory_extractor import (
    extract_memory
)


def chat(user_query):

    # Special memory inspection command
    if (
        "everything you've learned" in user_query.lower()
        or "show all memories" in user_query.lower()
        or "what do you know about" in user_query.lower()
    ):

        memories = get_memories()

        if not memories:
            return "I don't have any stored memories yet."

        result = "Here is everything I have learned:\n\n"

        for memory in memories:

            result += (
                f"🔹 Type: {memory[1]}\n"
                f"🔹 Value: {memory[2]}\n"
                f"🔹 Importance: {memory[3]}\n"
                f"🔹 Reason: {memory[4]}\n"
                f"{'-'*40}\n"
            )

        return result

    # Retrieve memories
    memory_context = get_memory_context()

    # Retrieve KB context
    rag_context = retrieve_context(user_query)

    # Combine both contexts
    combined_context = f"""
MEMORIES:

{memory_context}

KNOWLEDGE BASE:

{rag_context}
"""

    # Generate answer
    answer = generate_answer(
        user_query,
        combined_context
    )

    # Extract memory safely
    try:

        memory = extract_memory(
            user_query
        )

        print("\nEXTRACTED MEMORY:")
        print(memory)

        if memory:

            save_or_update_memory(
                memory["memory_type"],
                memory["value"],
                memory["importance"],
                memory["reason"]
            )

    except Exception as e:

        print("\nMEMORY SAVE ERROR:\n")
        print(e)

    return answer