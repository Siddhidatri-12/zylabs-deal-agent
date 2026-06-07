# Deal Intelligence Agent

An AI-powered Deal Intelligence Agent that combines:

* Retrieval Augmented Generation (RAG)
* Long-Term Memory
* Knowledge Base Search
* Deal Context Tracking
* Memory Dashboard
* FastAPI Backend
* Streamlit Frontend
* Gemini 2.5 Flash

The system helps sales teams retrieve company information, remember important deal details, track stakeholders, and generate context-aware responses across conversations.

---

# Features

## Knowledge Base Retrieval (RAG)

Retrieves relevant information from a Qdrant vector database using semantic search.

Examples:

* Company profiles
* Industry insights
* Deal intelligence
* Customer information

---

## Long-Term Memory

The agent automatically remembers important information shared by users.

Supported memory types:

* Account
* Stakeholder
* Pain Point
* Buying Signal
* Preference
* Deal Context

Example:

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

* Memory Type
* Value
* Importance Score
* Reason
* Created Timestamp
* Updated Timestamp

---

## Memory Search

Search memories by type.

Examples:

```text
Account
Stakeholder
Pain Point
Buying Signal
```

---

## Memory Deletion

Delete memories directly from the interface or via API endpoints.

Example:

```http
DELETE /memory/{value}
```

---

## Context-Aware Responses

The agent combines:

1. Long-Term Memory
2. Retrieved Knowledge Base Context

to generate more relevant responses.

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
               Gemini 2.5 Flash
                      │
                      ▼
                 AI Response
```

---

# Key Design Decisions

* Gemini 2.5 Flash was selected for fast and accurate response generation.
* Qdrant was used for semantic vector retrieval.
* SQLite was chosen for lightweight persistent memory storage.
* Memory updates prevent duplicate account records.
* Explainable memories store importance scores and reasons for transparency.

---

# Tech Stack

## Backend

* Python
* FastAPI

## Frontend

* Streamlit

## Vector Database

* Qdrant

## Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

## LLM

* Google Gemini 2.5 Flash
* Google AI Studio API

## Database

* SQLite

---

# Project Structure

```text
zylabs-deal-agent/
│
├── backend/
│   ├── __init__.py
│   ├── chat.py
│   ├── check_qdrant.py
│   ├── llm.py
│   ├── main.py
│   ├── memory.py
│   ├── memory_extractor.py
│   ├── qdrant_db.py
│   └── rag.py
│
├── streamlit.py
├── requirements.txt
├── README.md
└── .gitignore
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

## 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Generate your API key from Google AI Studio.

---

## 5. Start FastAPI

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

## 6. Start Streamlit

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

* Memory Ranking
* Memory Expiry
* Conversation History
* User Authentication
* Multi-Account Support
* Semantic Memory Search
* Feedback Loop
* CRM Integration
* Salesforce Integration
* HubSpot Integration
* Gemini Function Calling
* Hybrid Search (Vector + Keyword)
* Multi-Agent Deal Analysis

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

✅ Gemini 2.5 Flash Integration

✅ Context-Aware Responses

---

# Author

**Siddhidatri Singhal**

AI & Data Science Enthusiast

Built as part of the ZyLabs Deal Intelligence Agent Assignment.
