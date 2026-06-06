from backend.memory import (
    init_db,
    save_or_update_memory,
    get_memories
)

init_db()

save_or_update_memory(
    "account",
    "Acme Cyber",
    0.95,
    "Current account"
)

save_or_update_memory(
    "account",
    "CloudForge",
    0.95,
    "Current account changed"
)

print(get_memories())