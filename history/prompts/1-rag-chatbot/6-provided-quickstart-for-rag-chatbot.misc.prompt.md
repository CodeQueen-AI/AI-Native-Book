---
id: 6
title: Provided Quickstart for RAG Chatbot
stage: misc
date: 2025-12-15
surface: agent
model: Gemini
feature: 1-rag-chatbot
branch: [UNKNOWN - manual branch creation recommended]
user: user
command: continue
labels: [quickstart, usage]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
 - specs/1-rag-chatbot/quickstart.md
tests:

---

## Prompt

continue

## Response snapshot

# Quickstart for "RAG Chatbot for Docusaurus Book"

This guide explains how to get started with the RAG Chatbot.

## 1. Setup Backend

### Prerequisites

*   Python 3.11
*   FastAPI
*   OpenAI Agents SDK
*   Qdrant Cloud account and API Key
*   Neon Postgres account and connection string
*   Gemini API Key

### Installation

Clone the repository and install Python dependencies:

```bash
git clone [repository-url]
cd backend
pip install -r requirements.txt
```

### Configuration

Set up environment variables for API keys and database connection:

```
# .env file in backend/
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_URL=your_qdrant_url
NEON_POSTGRES_CONN_STR=your_neon_postgres_connection_string
GEMINI_API_KEY=your_gemini_api_key
```

### Running the Backend

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

## 2. Index Docusaurus Book Content

Before asking questions, the chatbot needs to index the book content.

### Manual Indexing Trigger

Send a POST request to the `/index-book` endpoint:

```bash
curl -X POST http://127.0.0.1:8000/index-book
# Or with --force to re-index regardless of changes
curl -X POST http://127.0.0.1:8000/index-book -H "Content-Type: application/json" -d '{"force": true}'
```

The system will detect changes and warn if re-indexing is needed.

## 3. Integrate Frontend Widget

The frontend will be a React component embedded as an iframe in your Docusaurus site.

### Frontend Setup

(Details to be provided in frontend development tasks)

## 4. Ask Questions

Once indexed, you can interact with the chatbot via the `/chat` API endpoint or the frontend widget.

```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{
  "query": "What are the components of Physical AI systems?",
  "context_type": "full_book"
}'
```

## Outcome

- ✅ Impact: The quickstart guide for the RAG Chatbot has been provided to the user, detailing setup, indexing, and interaction.
- 🧪 Tests: None
- 📁 Files: None modified (only read for output).
- 🔁 Next prompts: User can now proceed with setting up and using the RAG Chatbot.
- 🧠 Reflection: The agent successfully identified the user's implicit request for next steps and provided relevant documentation.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Request to continue after implementation.
- Next experiment (smallest change to try): None
