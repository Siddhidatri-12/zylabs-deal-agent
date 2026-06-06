# backend/test_insert.py

from backend.memory import (
    save_or_update_memory,
    get_memories
)

save_or_update_memory(
    "account",
    "CloudForge",
    0.95,
    "Current active account"
)

print(get_memories())