import json
import re
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


def extract_memory(user_message):

    # ==========================
    # ACCOUNT DETECTION
    # ==========================

    account_patterns = [

        r"working on\s+([A-Z][A-Za-z0-9&-]*(?:\s+[A-Z][A-Za-z0-9&-]*)*)",

        r"working\s+([A-Z][A-Za-z0-9&-]*(?:\s+[A-Z][A-Za-z0-9&-]*)*)",

        r"account is\s+([A-Z][A-Za-z0-9&-]*(?:\s+[A-Z][A-Za-z0-9&-]*)*)"
    ]

    for pattern in account_patterns:

        match = re.search(
            pattern,
            user_message
        )

        if match:

            return {
                "memory_type": "account",
                "value": match.group(1).strip(),
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

        response = model.generate_content(
            prompt
        )

        response_text = response.text

        print("\nRAW RESPONSE:\n")
        print(response_text)

        match = re.search(
            r"\{.*?\}",
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