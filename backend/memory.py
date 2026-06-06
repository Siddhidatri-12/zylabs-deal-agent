import sqlite3
import os

# Project root path
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Database folder path
DB_FOLDER = os.path.join(
    BASE_DIR,
    "database"
)

# Create database folder if it doesn't exist
os.makedirs(DB_FOLDER, exist_ok=True)

# Database file path
DB_NAME = os.path.join(
    DB_FOLDER,
    "memories.db"
)


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        memory_type TEXT,

        value TEXT,

        importance REAL,

        reason TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_memory(
    memory_type,
    value,
    importance,
    reason
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memories
        (
            memory_type,
            value,
            importance,
            reason
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            memory_type,
            value,
            importance,
            reason
        )
    )

    conn.commit()
    conn.close()


def get_memories():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM memories"
    )

    memories = cursor.fetchall()

    conn.close()

    return memories


def find_memory(memory_type):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM memories
        WHERE memory_type = ?
        """,
        (memory_type,)
    )

    memory = cursor.fetchone()

    conn.close()

    return memory


def update_memory(
    memory_type,
    value,
    importance,
    reason
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE memories
        SET
            value = ?,
            importance = ?,
            reason = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE memory_type = ?
        """,
        (
            value,
            importance,
            reason,
            memory_type
        )
    )

    conn.commit()

    conn.close()


def save_or_update_memory(
    memory_type,
    value,
    importance,
    reason
):

    existing = find_memory(memory_type)

    if existing:

        update_memory(
            memory_type,
            value,
            importance,
            reason
        )

        print("Memory Updated")

    else:

        save_memory(
            memory_type,
            value,
            importance,
            reason
        )

        print("Memory Created")

def get_memory_context():
    memories = get_memories()

    context = ""

    for memory in memories:

        context += (
            f"Type: {memory[1]}\n"
            f"Value: {memory[2]}\n"
            f"Reason: {memory[4]}\n\n"
        )

    return context


if __name__ == "__main__":

    init_db()

    print("Memory database created")

def get_memory_context():

    memories = get_memories()

    context = ""

    for memory in memories:

        context += (
            f"Type: {memory[1]}\n"
            f"Value: {memory[2]}\n"
            f"Reason: {memory[4]}\n\n"
        )

    return context

def delete_memory(value):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM memories
        WHERE value = ?
        """,
        (value,)
    )

    conn.commit()
    conn.close()