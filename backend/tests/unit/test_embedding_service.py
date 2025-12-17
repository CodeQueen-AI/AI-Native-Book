import pytest
from unittest.mock import MagicMock, patch
from backend.src.services.embedding_service import EmbeddingService

# Mock the genai module
@pytest.fixture(autouse=True)
def mock_genai_configure():
    with patch("google.generativeai.configure") as mock_configure:
        yield mock_configure

@pytest.fixture
def embedding_service():
    # We need to mock get_settings or ensure settings are correctly configured for tests
    with patch("backend.src.core.config.get_settings") as mock_get_settings:
        mock_settings = MagicMock()
        mock_settings.GEMINI_API_KEY = "test_api_key"
        mock_get_settings.return_value = mock_settings
        service = EmbeddingService()
        yield service

def test_generate_embedding_success(embedding_service):
    test_text = "This is a test sentence."
    mock_embedding_vector = [0.1, 0.2, 0.3]

    with patch("google.generativeai.embed_content") as mock_embed_content:
        mock_embed_content.return_value = {"embedding": mock_embedding_vector}
        embedding = embedding_service.generate_embedding(test_text)
        
        mock_embed_content.assert_called_once_with(
            model=embedding_service.model_name,
            content=test_text,
            task_type="RETRIEVAL_DOCUMENT"
        )
        assert embedding == mock_embedding_vector

def test_generate_embedding_failure(embedding_service):
    test_text = "This text will cause an error."

    with patch("google.generativeai.embed_content") as mock_embed_content:
        mock_embed_content.side_effect = Exception("API error")
        embedding = embedding_service.generate_embedding(test_text)
        
        assert embedding is None

def test_get_embedding_model_name(embedding_service):
    assert embedding_service.get_embedding_model_name() == "models/embedding-001"
