import json
import re
from ollama import chat


def extract_memory(user_message):

    # Detect account mentions like:
    # "I'm working on Acme Cyber"
    # "Actually I'm working CloudForge now"

    account_match = re.search(
        r"(?:working on|working)\s+([A-Z][A-Za-z0-9\s&-]+)",
        user_message
    )

    if account_match:

        return {
            "memory_type": "account",
            "value": account_match.group(1).strip(),
            "importance": 0.95,
            "reason": "Current active account"
        }

    prompt = f"""
You are a memory extraction system.

Extract information that should be remembered.

Allowed memory types:

- stakeholder
- pain_point
- buying_signal
- preference
- deal_context

If no memory exists return:

{{}}

Return ONLY valid JSON.

Message:

{user_message}
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

        response_text = response["message"]["content"]

        print("\nRAW RESPONSE:\n")
        print(response_text)

        match = re.search(
            r"\{.*\}",
            response_text,
            re.DOTALL
        )

        if not match:
            return None

        return json.loads(
            match.group()
        )

    except Exception as e:

        print("\nMEMORY EXTRACTION ERROR:\n")
        print(e)

        return None