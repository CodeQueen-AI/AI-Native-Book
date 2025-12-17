import pytest
from unittest.mock import MagicMock, patch
from backend.src.services.qdrant_service import QdrantService
from backend.src.models.data_models import Chunk, ChunkMetadata, Embedding
from qdrant_client.http.models import PointStruct, ScoredPoint, Payload, Distance, VectorParams
from typing import List

@pytest.fixture
def mock_qdrant_client():
    with patch("qdrant_client.QdrantClient") as MockQdrantClient:
        mock_client = MockQdrantClient.return_value
        yield mock_client

@pytest.fixture
def qdrant_service(mock_qdrant_client):
    with patch("backend.src.core.config.get_settings") as mock_get_settings:
        mock_settings = MagicMock()
        mock_settings.QDRANT_URL = "http://test_url"
        mock_settings.QDRANT_API_KEY = "test_api_key"
        mock_get_settings.return_value = mock_settings
        service = QdrantService()
        service.client = mock_qdrant_client # Inject the mock client
        yield service

def test_recreate_collection(qdrant_service, mock_qdrant_client):
    vector_size = 768
    qdrant_service.recreate_collection(vector_size)
    mock_qdrant_client.delete_collection.assert_called_once_with(collection_name="docusaurus_chunks")
    mock_qdrant_client.recreate_collection.assert_called_once_with(
        collection_name="docusaurus_chunks",
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )

def test_upsert_chunks(qdrant_service, mock_qdrant_client):
    chunks = [
        Chunk(id="1", text="text1", metadata=ChunkMetadata(file_path="f1.md"), embedding=[0.1]*768),
        Chunk(id="2", text="text2", metadata=ChunkMetadata(file_path="f2.md"), embedding=[0.2]*768)
    ]
    qdrant_service.upsert_chunks(chunks)
    mock_qdrant_client.upsert.assert_called_once()
    assert len(mock_qdrant_client.upsert.call_args[1]['points']) == 2

def test_search_chunks(qdrant_service, mock_qdrant_client):
    query_embedding = [0.5] * 768
    mock_search_results = [
        ScoredPoint(id=1, version=1, score=0.9, payload=Payload({"text": "found chunk 1", "file_path": "a.md", "heading": "H1"}), vector=None),
        ScoredPoint(id=2, version=1, score=0.8, payload=Payload({"text": "found chunk 2", "file_path": "b.md"}), vector=None)
    ]
    mock_qdrant_client.search.return_value = mock_search_results

    found_chunks = qdrant_service.search_chunks(query_embedding, limit=2)
    
    mock_qdrant_client.search.assert_called_once_with(
        collection_name="docusaurus_chunks",
        query_vector=query_embedding,
        limit=2,
        with_payload=True,
        with_vectors=False
    )
    assert len(found_chunks) == 2
    assert found_chunks[0].text == "found chunk 1"
    assert found_chunks[0].metadata.file_path == "a.md"
    assert found_chunks[1].text == "found chunk 2"
