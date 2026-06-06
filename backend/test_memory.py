from backend.memory import (
    init_db,
    save_memory,
    get_memories
)

init_db()

save_memory(
    "account",
    "Acme Cyber",
    0.95,
    "Active account being worked"
)

print(get_memories())