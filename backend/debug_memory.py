# backend/debug_memory.py

from memory import *

print("Functions loaded successfully")

save_or_update_memory(
    "account",
    "CloudForge",
    0.95,
    "Current active account"
)

print(get_memories())