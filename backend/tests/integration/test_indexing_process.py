import pytest
from unittest.mock import MagicMock, patch
from backend.src.services.indexing_service import IndexingService # Assuming this will be implemented
from backend.src.models.data_models import ChunkMetadata, Chunk

@pytest.fixture
def mock_qdrant_service():
    with patch("backend.src.services.qdrant_service.QdrantService") as MockQdrantService:
        mock_service = MockQdrantService.return_value
        yield mock_service

@pytest.fixture
def mock_neon_service():
    with patch("backend.src.services.neon_service.NeonService") as MockNeonService:
        mock_service = MockNeonService.return_value
        yield mock_service

@pytest.fixture
def mock_embedding_service():
    with patch("backend.src.services.embedding_service.EmbeddingService") as MockEmbeddingService:
        mock_service = MockEmbeddingService.return_value
        # Mock embedding generation to return a dummy vector
        mock_service.generate_embedding.return_value = [0.1] * 1536 # Example vector size
        mock_service.get_embedding_model_name.return_value = "models/embedding-001"
        yield mock_service

@pytest.fixture
def mock_chunking_service():
    with patch("backend.src.services.chunking_service.ChunkingService") as MockChunkingService:
        mock_service = MockChunkingService.return_value
        # Mock chunking to return predefined chunks
        mock_service.chunk_text.return_value = [
            Chunk(id="1", text="chunk 1", metadata=ChunkMetadata(file_path="test.md", heading="H1")),
            Chunk(id="2", text="chunk 2", metadata=ChunkMetadata(file_path="test.md", heading="H1"))
        ]
        yield mock_service

def test_full_book_indexing_process(
    mock_qdrant_service, mock_neon_service, mock_embedding_service, mock_chunking_service
):
    """
    T021: Integration test for full book indexing process.
    """
    test_book_content_dir = "/tmp/mock_docusaurus_docs"
    test_md_file_path = f"{test_book_content_dir}/test.md"
    
    # Mock file system operations if needed, or create dummy files
    with patch("backend.src.core.file_io.list_markdown_files", return_value=[test_md_file_path]):
        with patch("backend.src.core.file_io.read_file_content", return_value="Some test content."):
            indexing_service = IndexingService(
                qdrant_service=mock_qdrant_service,
                neon_service=mock_neon_service,
                embedding_service=mock_embedding_service,
                chunking_service=mock_chunking_service
            )
            indexing_service.run_indexing_process(book_content_dir=test_book_content_dir)

            mock_qdrant_service.recreate_collection.assert_called_once()
            mock_qdrant_service.upsert_chunks.assert_called_once()
            mock_neon_service.create_tables.assert_called_once()
            mock_neon_service.add_chunk_info.assert_called() # Called for each chunk
