import pytest
from backend.src.services.chunking_service import ChunkingService
from backend.src.models.data_models import ChunkMetadata

@pytest.fixture
def chunking_service():
    return ChunkingService(chunk_size=10, chunk_overlap=2) # Smaller size for testing

def test_chunking_basic(chunking_service):
    text = "This is a simple sentence to test the basic chunking logic."
    chunks = chunking_service.chunk_text(text, "test.md", {"heading": "Test"})
    assert len(chunks) > 1 # Expect more than one chunk
    assert all(chunk.metadata.file_path == "test.md" for chunk in chunks)
    assert chunks[0].text.startswith("This is a simple")
    # Check for overlap (approximate due to word boundaries)
    assert "logic." in chunks[-1].text # Last word should be in the last chunk

def test_chunking_empty_text(chunking_service):
    text = ""
    chunks = chunking_service.chunk_text(text, "empty.md")
    assert len(chunks) == 0

def test_chunking_short_text(chunking_service):
    text = "Short text"
    chunks = chunking_service.chunk_text(text, "short.md")
    assert len(chunks) == 1
    assert chunks[0].text == "Short text"

def test_chunking_metadata_propagation(chunking_service):
    text = "Some text."
    metadata = {"heading": "Intro", "page": 1}
    chunks = chunking_service.chunk_text(text, "meta.md", metadata)
    assert len(chunks) == 1
    assert chunks[0].metadata.heading == "Intro"
    assert chunks[0].metadata.page == 1
    assert chunks[0].metadata.file_path == "meta.md"
