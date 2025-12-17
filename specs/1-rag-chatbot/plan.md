# Implementation Plan: RAG Chatbot for Docusaurus Book

**Branch**: `1-rag-chatbot` (manual creation needed)
**Date**: 2025-12-15
**Spec**: `../spec.md`

## Summary

This plan outlines the technical approach for implementing a RAG (Retrieval Augmented Generation) chatbot that answers questions based on a Docusaurus book, with support for both full-book and selected text queries.

## Technical Context

-   **Language/Version**: Python 3.14.0 for backend (FastAPI, OpenAI Agents SDK), JavaScript/TypeScript for frontend (React/iframe widget).
-   **Primary Dependencies**: FastAPI (latest stable), OpenAI Agents SDK (latest stable), Qdrant Client (latest stable), Psycopg2/SQLAlchemy (latest stable), Gemini API Client (latest stable), React (latest stable).
-   **Storage**: Qdrant Cloud (for embeddings + metadata), Neon Postgres (for book/chunk info).
-   **Testing**: `pytest` for Python backend, `jest`/`react-testing-library` for React frontend.
-   **Target Platform**: Local FastAPI server for backend, Docusaurus UI (browser) for frontend.
-   **Project Type**: Backend API (Python/FastAPI) + Frontend Widget (React/iframe).
-   **Performance Goals**: Initial indexing within 5 minutes, chatbot response under 5 seconds.
-   **Constraints**: No Docker for deployment. Works inside Docusaurus UI.
-   **Scale/Scope**: Docusaurus book up to a moderate size (e.g., hundreds of pages).

## Constitution Check

-   [X] **Spec-Driven Development**: `spec.md` exists and is referenced.
-   [X] **Architectural Planning**: This `plan.md` is being created.
-   [ ] **Task-Based Execution**: A `tasks.md` will be created from this plan.
-   [X] **Record Keeping**: PHRs and ADRs will be created as needed.
-   [ ] **Test-Driven Development**: Test creation tasks will be included in `tasks.md`.

## Project Structure

### Documentation (this feature)

```text
specs/1-rag-chatbot/
├── plan.md              # This file
├── research.md          # To be generated
├── data-model.md        # To be generated
├── contracts/           # To be generated
└── quickstart.md        # To be generated
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # API endpoints
│   ├── services/            # Business logic (e.g., RAG pipeline, Qdrant/Neon interaction)
│   ├── models/              # Data models (Pydantic, ORM)
│   └── core/                # Configuration, utilities, LLM integration
└── tests/
    ├── unit/
    └── integration/

frontend/
├── src/
│   ├── components/          # React components for the chatbot widget
│   ├── hooks/               # React hooks
│   └── App.tsx              # Main application for the iframe widget
└── tests/
```

**Structure Decision**: A monorepo structure with separate `backend/` (Python/FastAPI) and `frontend/` (React/iframe) directories.

## Complexity Tracking

No violations of constitutional principles.
