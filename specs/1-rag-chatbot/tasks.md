---

description: "Task list for 'RAG Chatbot for Docusaurus Book' feature"
---

# Tasks: RAG Chatbot for Docusaurus Book

**Input**: Design documents from `specs/1-rag-chatbot/`
**Prerequisites**: `plan.md` (required), `spec.md` (required for user stories), `data-model.md`, `contracts/api.yaml`, `research.md`, `quickstart.md`

**Tests**: Test tasks will be generated. The feature involves complex integration and AI models, making robust testing critical.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure
- [X] T001 [P] Create `backend/` and `frontend/` root directories
- [X] T002 [P] Initialize Python backend project in `backend/` with `pyproject.toml` (Python 3.14.0)
- [X] T003 [P] Configure `backend/pyproject.toml` with `FastAPI`, `OpenAI Agents SDK`, `Qdrant Client`, `Psycopg2`, `SQLAlchemy`, `Gemini API Client`, `pytest` dependencies
- [X] T004 [P] Initialize React frontend project in `frontend/` (using `create-react-app` or similar)
- [X] T005 [P] Configure `frontend/package.json` with `jest`/`react-testing-library` dependencies
- [X] T006 Create `backend/src/` and subdirectories (`api/`, `services/`, `models/`, `core/`)
- [X] T007 Create `frontend/src/` and subdirectories (`components/`, `hooks/`)
- [X] T008 Create `backend/tests/` and subdirectories (`unit/`, `integration/`)
- [X] T009 Create `frontend/tests/`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T010 Implement FastAPI application entry point in `backend/src/main.py`
- [X] T011 [P] Implement base data models (Pydantic) for `Chunk`, `Embedding`, `UserQuery`, `ChatbotResponse` in `backend/src/models/data_models.py` (based on `data-model.md`)
- [X] T012 [P] Implement `file_io` utility for reading Docusaurus Markdown files in `backend/src/core/file_io.py`
- [X] T013 [P] Configure environment variable loading for API keys and DB connection in `backend/src/core/config.py`
- [X] T014 [P] Set up Qdrant client connection and basic collection management in `backend/src/services/qdrant_service.py`
- [X] T015 [P] Set up Neon Postgres connection and basic table management in `backend/src/services/neon_service.py`
- [X] T016 [P] Implement text chunking logic (150-400 words, small overlap) in `backend/src/services/chunking_service.py`
- [X] T017 [P] Implement embedding generation logic (Gemini embedding model) in `backend/src/services/embedding_service.py`
- [X] T018 Implement basic API routes (`/chat`, `/index-book`) in `backend/src/api/` (based on `contracts/api.yaml`)

## Phase 3: User Story 3 - Read and Index Book Content (Priority: P1) 🎯 MVP for Indexing

**Goal**: Read Docusaurus book content, chunk it, create embeddings, and store in Qdrant and Neon.

**Independent Test**: Verify that Qdrant and Neon contain indexed book content with correct metadata after running the indexing process.

### Tests for User Story 3

- [X] T019 [P] [US3] Unit test `chunking` logic for various text inputs in `backend/tests/unit/test_chunking_service.py`
- [X] T020 [P] [US3] Unit test `embedding` generation for consistency and correctness in `backend/tests/unit/test_embedding_service.py`
- [X] T021 [US3] Integration test: full book indexing process populates Qdrant and Neon in `backend/tests/integration/test_indexing_process.py`
- [X] T022 [US3] Integration test: `index-book` API endpoint triggers indexing and returns success in `backend/tests/integration/test_api_endpoints.py`

### Implementation for User Story 3

- [X] T023 [US3] Implement logic to read Docusaurus Markdown files from `/book_source/docs` in `backend/src/services/indexing_service.py`
- [ ] T024 [US3] Integrate `chunking_service` and `embedding_service` into `indexing_service`
- [ ] T025 [US3] Implement logic to store chunks and embeddings in Qdrant with metadata in `backend/src/services/qdrant_service.py`
- [ ] T026 [US3] Implement logic to store book/chunk info in Neon Postgres in `backend/src/services/neon_service.py`
- [X] T027 [US3] Extend `/index-book` API endpoint to trigger the `indexing_service`
- [ ] T028 [US3] Implement change detection for Docusaurus book content and `specify.txt` to warn user if re-indexing is needed (Hybrid approach) in `backend/src/services/indexing_service.py`

## Phase 4: User Story 4 & 5 - Retrieve & Generate Answer (Priority: P1) 🎯 MVP for Chatbot

**Goal**: Retrieve relevant chunks from Qdrant and generate answers using the Gemini model.

**Independent Test**: Ask a question whose answer is in the indexed content and verify chatbot returns correct answer with source chunks.

### Tests for User Story 4 & 5

- [X] T029 [P] [US4/5] Unit test `retrieval` logic for semantic similarity in `backend/tests/unit/test_qdrant_service.py`
- [X] T030 [P] [US4/5] Unit test `answer generation` with mock LLM for coherence and context adherence in `backend/tests/unit/test_gemini_service.py`
- [X] T031 [US4/5] Integration test: `/chat` API endpoint returns correct answer with sources for full-book query in `backend/tests/integration/test_api_endpoints.py`

### Implementation for User Story 4 & 5

- [X] T032 [US4] Implement query embedding generation in `backend/src/services/embedding_service.py`
- [X] T033 [US4] Implement logic to retrieve best chunks from Qdrant based on query embedding in `backend/src/services/qdrant_service.py`
- [X] T034 [US5] Implement prompt engineering to add chunks to LLM prompt in `backend/src/services/gemini_service.py`
- [X] T035 [US5] Implement Gemini model invocation for answer generation in `backend/src/services/gemini_service.py`
- [X] T036 [US4/5] Extend `/chat` API endpoint to integrate retrieval and answer generation services in `backend/src/api/chatbot_api.py` (or `main.py`)
- [X] T037 [US4/5] Implement logic to display answers with source text in the API response in `backend/src/api/chatbot_api.py`

## Phase 5: User Story 1 & 2 - Full Book & Selected Text Query (Priority: P1)

**Goal**: Ensure chatbot works for both full-book and selected text queries.

**Independent Test**: Verify both query types yield correct, context-specific answers.

### Tests for User Story 1 & 2

- [X] T038 [US1/2] Integration test: `/chat` API for selected text query returns context-specific answer in `backend/tests/integration/test_api_endpoints.py`
- [X] T039 [P] [US1/2] Frontend unit test for rendering full-book query in `frontend/tests/unit/test_chatbot_widget.tsx`
- [X] T040 [P] [US1/2] Frontend unit test for handling selected text query input in `frontend/tests/unit/test_chatbot_widget.tsx`

### Implementation for User Story 1 & 2

- [X] T041 [US1/2] Implement logic in backend to filter retrieval based on selected text context in `backend/src/services/qdrant_service.py`
- [X] T042 [US1/2] Implement React chatbot widget UI (`frontend/src/components/ChatbotWidget.tsx`)
- [X] T043 [US1/2] Implement React widget logic to send full-book queries to backend in `frontend/src/hooks/useChatbot.ts`
- [X] T044 [US1/2] Implement React widget logic to send selected text queries to backend in `frontend/src/hooks/useChatbot.ts`
- [X] T045 [US1/2] Implement iframe integration into Docusaurus (frontend deployment setup)

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T046 [P] Code cleanup and refactoring across `backend/` and `frontend/`
- [X] T047 [P] Performance optimization for Qdrant/Neon queries
- [X] T048 [P] Implement comprehensive error handling and logging for both backend and frontend
- [X] T049 [P] Document API endpoints with OpenAPI/Swagger (`backend/main.py`)
- [X] T050 [P] Update `quickstart.md` with final installation and usage instructions
- [X] T051 [P] Set up CI/CD pipelines for backend and frontend (if applicable, or mock)

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
-   **User Stories (Phase 3+)**: All depend on Foundational phase completion
    -   US3 (Phase 3) is a prerequisite for US4 & US5 (Phase 4).
    -   US4 & US5 (Phase 4) is a prerequisite for US1 & US2 (Phase 5).
-   **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

-   **US3 (P1) Indexing**: No dependencies on other stories; foundational.
-   **US4 & US5 (P1) Retrieve & Generate**: Depends on US3 for indexed data.
-   **US1 & US2 (P1) Full Book & Selected Text Query**: Depends on US4 & US5 for core Q&A functionality.

### Within Each User Story

-   Tests MUST be written and FAIL before implementation
-   Models/Entities before services
-   Services before API endpoints/UI integration
-   Core implementation before integration
-   Story complete before moving to next priority

## Implementation Strategy

### MVP First (Phase 3)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 3 (Indexing)
4.  **STOP and VALIDATE**: Test indexing process independently (Qdrant/Neon populated)
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 3 (Indexing) → Test independently → Deploy/Demo (Indexing MVP!)
3.  Add User Story 4 & 5 (Retrieve & Generate) → Test independently → Deploy/Demo (Backend Chatbot MVP!)
4.  Add User Story 1 & 2 (Full Book & Selected Text Query) → Test independently → Deploy/Demo (Full Chatbot MVP!)

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: Phase 3 (Indexing Backend)
    -   Developer B: Phase 4 (Chatbot Core Backend)
    -   Developer C: Phase 5 (Frontend + API Integration)
3.  Stories complete and integrate independently
