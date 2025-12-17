# Feature Specification: RAG Chatbot for Docusaurus Book

**Feature Branch**: `1-rag-chatbot` (manual creation needed)
**Created**: 2025-12-15
**Status**: Draft
**Input**: User description from `specify.txt`

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a Question about the Full Book (Priority: P1)

As a user, I want to ask questions about the entire Docusaurus book content and receive accurate answers with source text, so I can learn from the material effectively.

**Why this priority**: This is the primary function of a RAG chatbot.

**Independent Test**: Ask a question whose answer is contained within the full book content and verify that the chatbot provides a correct answer and relevant source chunks.

**Acceptance Scenarios**:

1.  **Given** the chatbot has indexed the full Docusaurus book, **When** I ask a question about the book content, **Then** the chatbot provides a relevant answer.
2.  **Given** the chatbot provides an answer, **Then** it also shows the source text (chunks) from which the answer was generated.

### User Story 2 - Ask a Question about Selected Text (Priority: P1)

As a user, I want to ask questions about only the currently selected text in the Docusaurus UI and receive accurate answers with source text, so I can get context-specific information.

**Why this priority**: This is a core functionality for context-aware Q&A.

**Independent Test**: Select a specific passage of text in the Docusaurus UI, ask a question relevant only to that passage, and verify that the chatbot's answer is based solely on the selected text and shows correct source chunks.

**Acceptance Scenarios**:

1.  **Given** I have selected a text portion in the Docusaurus UI, **When** I ask a question, **Then** the chatbot's answer is based *only* on the selected text.
2.  **Given** the chatbot provides an answer based on selected text, **Then** it shows the source text (chunks) from the selected portion.

### User Story 3 - Read and Index Book Content (Priority: P1)

As the chatbot system, I need to read the full Docusaurus book content, break it into small chunks, create embeddings, and store them in Qdrant and Neon, to prepare for answering user questions.

**Why this priority**: Essential backend setup for RAG functionality.

**Independent Test**: Verify that the Qdrant and Neon databases contain indexed book content, with appropriate chunking, embeddings, and metadata (heading, page, index).

**Acceptance Scenarios**:

1.  **Given** Docusaurus book content is available, **When** the indexing process runs, **Then** the content is broken into chunks of 150-400 words with small overlap.
2.  **Given** chunks are created, **Then** embeddings are generated for each chunk and stored in Qdrant along with metadata (heading, page, index).
3.  **Given** book/chunk information is available, **Then** relevant data is stored in Neon Postgres.

### User Story 4 - Retrieve Relevant Information (Priority: P1)

As the chatbot system, when a user asks a question, I need to retrieve the most relevant chunks from Qdrant, to provide context for generating an answer.

**Why this priority**: Core RAG functionality.

**Independent Test**: For a given question, verify that the system retrieves semantically relevant chunks from Qdrant.

**Acceptance Scenarios**:

1.  **Given** a user question, **When** the system queries Qdrant, **Then** it retrieves the top N (e.g., 3-5) most relevant chunks.

### User Story 5 - Generate Answer (Priority: P1)

As the chatbot system, I need to generate a final answer to a user's question using the retrieved chunks and the Gemini model, so the user receives a comprehensive response.

**Why this priority**: Final step in providing a user-facing answer.

**Independent Test**: Provide a question and relevant chunks, then verify that the Gemini model produces a coherent and accurate answer based on the provided context.

**Acceptance Scenarios**:

1.  **Given** a user question and retrieved chunks, **When** Gemini model is prompted, **Then** it generates a final, coherent answer.

**Edge Cases**:

-   What happens if no relevant chunks are retrieved?
    -   System should respond with "I don't have enough information to answer that question from the provided content."
-   What happens if `specify.txt` is modified, and the book content changes?
    -   System should warn the user if changes are detected and re-indexing is needed, and re-indexing will be manually triggered.
-   What happens if the Docusaurus book content is empty or unreadable?
    -   System should report an error and not proceed with indexing.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: System MUST read and index Docusaurus book content (`.md` files in `/book_source/docs`).
-   **FR-002**: System MUST break text into chunks of 150-400 words with small overlap.
-   **FR-003**: System MUST create embeddings for chunks and store them in Qdrant with metadata (heading, page, index).
-   **FR-004**: System MUST store book/chunk information in Neon Postgres.
-   **FR-005**: System MUST retrieve the most relevant chunks from Qdrant based on user query embeddings.
-   **FR-006**: System MUST generate answers using the Gemini model, incorporating retrieved chunks into the LLM prompt.
-   **FR-007**: System MUST display answers along with their source text (chunks).
-   **FR-008**: System MUST support answering questions based on the full book content.
-   **FR-009**: System MUST support answering questions based on selected text only (e.g., from Docusaurus UI iframe widget).
-   **FR-010**: System MUST be deployable as a local FastAPI server (no Docker).
-   **FR-011**: System MUST work as a React/iframe widget within the Docusaurus UI.

### Key Entities *(include if feature involves data)*

-   **Docusaurus Book Content**: Markdown files (`.md`) located in `/book_source/docs`.
-   **Chunk**: A small segment of text (150-400 words with overlap) from the book content.
-   **Embedding**: A vector representation of a chunk of text.
-   **Qdrant**: Vector database for storing embeddings and metadata.
-   **Neon Postgres**: Relational database for storing book/chunk information.
-   **Gemini Model**: LLM used for answer generation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: Chatbot answers are correct (factually accurate and relevant to the question).
-   **SC-002**: Chatbot functions correctly for both full-book and highlighted text queries.
-   **SC-003**: Chatbot reliably shows source chunks for generated answers.
-   **SC-004**: Initial indexing of the Docusaurus book completes within 5 minutes.
-   **SC-005**: Chatbot response time for a typical query (retrieve + generate) is under 5 seconds.
