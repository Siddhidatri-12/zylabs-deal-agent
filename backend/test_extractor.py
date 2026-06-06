# backend/test_extractor.py

from backend.memory_extractor import extract_memory

message = "I'm working Acme Cyber this quarter."

memory = extract_memory(message)

print(memory)