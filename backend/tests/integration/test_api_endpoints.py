import pytest
import httpx # For making HTTP requests to FastAPI
from unittest.mock import patch, MagicMock
from backend.src.main import app # Assuming app is imported from main
from backend.src.models.data_models import IndexBookRequest

@pytest.fixture(scope="module")
async def async_client():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture
def mock_indexing_service():
    with patch("backend.src.services.indexing_service.IndexingService") as MockIndexingService:
        mock_service = MockIndexingService.return_value
        yield mock_service

@pytest.mark.asyncio
async def test_index_book_endpoint_success(async_client, mock_indexing_service):
    """
    T022: Integration test for /index-book API endpoint.
    """
    response = await async_client.post("/index-book", json={"force": False})

    assert response.status_code == 200
    assert response.json()["message"] == "Indexing process started."
    mock_indexing_service.run_indexing_process.assert_called_once_with(
        book_content_dir=app.state.book_content_dir, # Assuming this is set in app state
        force_reindex=False
    )

@pytest.mark.asyncio
async def test_index_book_endpoint_force_success(async_client, mock_indexing_service):
    """
    T022: Integration test for /index-book API endpoint with force=True.
    """
    response = await async_client.post("/index-book", json={"force": True})

    assert response.status_code == 200
    assert response.json()["message"] == "Indexing process started."
    mock_indexing_service.run_indexing_process.assert_called_once_with(
        book_content_dir=app.state.book_content_dir, # Assuming this is set in app state
        force_reindex=True
    )

# Add test for /chat endpoint later (T031, T038)

@pytest.fixture
def mock_embedding_service():
    with patch("backend.src.services.embedding_service.EmbeddingService") as MockEmbeddingService:
        mock_service = MockEmbeddingService.return_value
        mock_service.generate_embedding.return_value = [0.1] * 1536 # Dummy embedding
        yield mock_service

@pytest.fixture
def mock_qdrant_service_chat(): # Differentiate from indexing mock
    with patch("backend.src.services.qdrant_service.QdrantService") as MockQdrantService:
        mock_service = MockQdrantService.return_value
        # Mock search_chunks to return dummy data
        mock_service.search_chunks.return_value = [
            Chunk(
                id="chunk1", 
                text="Physical AI involves AI systems interacting with the real world.", 
                metadata=ChunkMetadata(file_path="intro.md", heading="What is Physical AI")
            )
        ]
        yield mock_service

@pytest.fixture
def mock_gemini_service():
    with patch("backend.src.services.gemini_service.GeminiService") as MockGeminiService:
        mock_service = MockGeminiService.return_value
        mock_service.generate_answer.return_value = "Physical AI is about AI interacting with the real world."
        yield mock_service

@pytest.mark.asyncio
async def test_chat_endpoint_full_book_query(
    async_client,
    mock_embedding_service,
    mock_qdrant_service_chat,
    mock_gemini_service
):
    """
    T031: Integration test for /chat API endpoint with full-book query.
    """
    query_payload = {"query": "What is Physical AI?", "context_type": "full_book"}
    response = await async_client.post("/chat", json=query_payload)

    assert response.status_code == 200
    json_response = response.json()
    assert "answer" in json_response
    assert "source_chunks" in json_response
    assert len(json_response["source_chunks"]) > 0
    assert json_response["answer"] == "Physical AI is about AI interacting with the real world."

    # Verify service calls
    mock_embedding_service.generate_embedding.assert_called_once_with(query_payload["query"])
    mock_qdrant_service_chat.search_chunks.assert_called_once() # Args will be checked more specifically in unit tests
    mock_gemini_service.generate_answer.assert_called_once_with(query_payload["query"], mock_qdrant_service_chat.search_chunks.return_value)

@pytest.mark.asyncio
async def test_chat_endpoint_selected_text_query(
    async_client,
    mock_embedding_service,
    mock_qdrant_service_chat,
    mock_gemini_service
):
    """
    T038: Integration test for /chat API endpoint with selected text query.
    """
    selected_text = "Physical AI involves AI systems designed to interact with the real world."
    query_payload = {"query": "What is Physical AI?", "context_type": "selected_text", "selected_text": selected_text}
    
    # Mock search_chunks to simulate filtering by selected_text
    mock_qdrant_service_chat.search_chunks.return_value = [
        Chunk(
            id="chunk_selected", 
            text=selected_text, 
            metadata=ChunkMetadata(file_path="intro.md", heading="What is Physical AI")
        )
    ]

    response = await async_client.post("/chat", json=query_payload)

    assert response.status_code == 200
    json_response = response.json()
    assert "answer" in json_response
    assert "source_chunks" in json_response
    assert len(json_response["source_chunks"]) > 0
    assert json_response["source_chunks"][0]["text"] == selected_text

    mock_embedding_service.generate_embedding.assert_called_once_with(query_payload["query"])
    # A more specific mock for qdrant_service.search_chunks should be implemented for context filtering
    mock_qdrant_service_chat.search_chunks.assert_called_once()
    mock_gemini_service.generate_answer.assert_called_once_with(query_payload["query"], mock_qdrant_service_chat.search_chunks.return_value)


