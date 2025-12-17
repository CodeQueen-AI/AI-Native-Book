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
uvicorn src.main:app --reload

without cd backend
uvicorn backend.src.main:app --reload

## 2. Index Docusaurus Book Content

Before asking questions, the chatbot needs to index the book content.

### Manual Indexing Trigger

Send a POST request to the `/index-book` endpoint:

```bash
curl -X POST http://127.0.0.1:8000/index-book
# Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/index-book
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/index-book

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
# curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{
#   "query": "What are the components of Physical AI systems?",
#   "context_type": "full_book"
# }'
```
```bash
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/chat `-Body (@{query="What is Physical AI?"; context_type="full_book"} | ConvertTo-Json) `-ContentType "application/json"
```