# Deal Intelligence Agent

An AI-powered Deal Intelligence Agent that combines:

- Retrieval Augmented Generation (RAG)
- Long-Term Memory
- Knowledge Base Search
- Deal Context Tracking
- Memory Dashboard
- FastAPI Backend
- Streamlit Frontend

The system helps sales teams retrieve company information, remember important deal details, track stakeholders, and provide contextual responses across conversations.

---

# Features

## Knowledge Base Retrieval (RAG)

Retrieves relevant information from a Qdrant vector database using semantic search.

Examples:

- Company profiles
- Industry insights
- Deal intelligence
- Customer information

---

## Long-Term Memory

The agent automatically remembers important information shared by users.

Supported memory types:

- Account
- Stakeholder
- Pain Point
- Buying Signal
- Preference
- Deal Context

Examples:

User:

```text
I'm working on Acme Cyber.
```

Stored Memory:

```json
{
  "memory_type": "account",
  "value": "Acme Cyber"
}
```

---

## Memory Updating

The agent updates existing memories instead of creating duplicates.

Example:

```text
I'm working on Acme Cyber.
```

Later:

```text
Actually I'm working on CloudForge now.
```

The account memory is updated automatically.

---

## Memory Dashboard

View all stored memories in real time through the Streamlit interface.

Information displayed:

- Memory Type
- Value
- Importance Score
- Reason
- Created Timestamp
- Updated Timestamp

---

## Memory Search

Search memories by type.

Examples:

```text
Find account memories
```

```text
Find stakeholder memories
```

---

## Memory Deletion

Delete memories using API endpoints.

Example:

```http
DELETE /memory/{value}
```

---

## Context-Aware Responses

The agent combines:

1. Long-Term Memory
2. Retrieved Knowledge Base Context

to generate more relevant answers.

Memory is prioritized whenever applicable.

---

# Architecture

```text
                    User
                      │
                      ▼
               Streamlit UI
                      │
                      ▼
                 FastAPI
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
   Memory System              RAG System
      SQLite                    Qdrant
        │                          │
        └─────────────┬────────────┘
                      ▼
                    Ollama
                      │
                      ▼
                 AI Response
```

---

# Tech Stack

## Backend

- Python
- FastAPI

## Frontend

- Streamlit

## Vector Database

- Qdrant

## Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

## LLM

- Ollama
- Llama 3.2

## Database

- SQLite

---

# Project Structure

```text
zylabs-deal-agent/
│
├── backend/
│   ├── main.py
│   ├── chat.py
│   ├── rag.py
│   ├── llm.py
│   ├── memory.py
│   ├── memory_extractor.py
│   ├── check_qdrant.py
│   └── ingest.py
│
├── database/
│   └── memories.db
│
├── streamlit.py
│
├── requirements.txt
│
└── README.md
```

---

# Setup

## 1. Clone Repository

```bash
git clone <repository_url>
cd zylabs-deal-agent
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Start Qdrant

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## 4. Create Knowledge Base

Run ingestion script:

```bash
python backend/ingest.py
```

---

## 5. Start Ollama

```bash
ollama serve
```

Verify model:

```bash
ollama list
```

Expected:

```text
llama3.2:3b
```

---

## 6. Start FastAPI

```bash
uvicorn backend.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 7. Start Streamlit

```bash
streamlit run streamlit.py
```

---

# API Endpoints

## Chat

```http
POST /chat
```

Request:

```json
{
  "message": "Tell me about Acme Cyber"
}
```

---

## Get All Memories

```http
GET /memories
```

---

## Delete Memory

```http
DELETE /memory/{value}
```

Example:

```http
DELETE /memory/Acme Cyber
```

---

# Example Workflow

### Store Memory

User:

```text
I'm working on Acme Cyber.
```

Memory Created:

```json
{
  "memory_type": "account",
  "value": "Acme Cyber"
}
```

---

### Add Stakeholder

User:

```text
Sarah Johnson is VP of Sales.
```

Memory Created:

```json
{
  "memory_type": "stakeholder",
  "value": "Sarah Johnson"
}
```

---

### Ask Contextual Question

User:

```text
Which account am I currently working on?
```

Response:

```text
You are currently working on Acme Cyber.
```

---

# Future Improvements

- Memory Ranking
- Memory Expiry
- Conversation History
- User Authentication
- Multi-Account Support
- Semantic Memory Search
- Feedback Loop
- CRM Integration
- Salesforce Integration
- HubSpot Integration

---

# Assignment Objectives Covered

✅ Knowledge Base Retrieval

✅ Vector Search with Qdrant

✅ Long-Term Memory

✅ Memory Update Logic

✅ Memory Search

✅ Memory Deletion

✅ FastAPI Backend

✅ Streamlit Frontend

✅ LLM Integration

✅ Context-Aware Responses

---

# Author

**Siddhidatri Singhal**

AI & Data Science Enthusiast

Built as part of the ZyLabs Deal Intelligence Agent Assignment.