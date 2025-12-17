# import httpx
# from typing import List, Optional
# from ..core.config import get_settings

# class EmbeddingService:
#     def __init__(self):
#         self.settings = get_settings()
#         self.openrouter_api_key = self.settings.OPENROUTER_API_KEY
#         self.openrouter_embedding_model_name = self.settings.OPENROUTER_EMBEDDING_MODEL_NAME
#         self.openrouter_api_base = "https://openrouter.ai/api/v1/embeddings"

#     async def generate_embedding(self, text: str) -> Optional[List[float]]:
#         """Generates an embedding for a given text using an OpenRouter-compatible embedding model."""
#         headers = {
#             "Authorization": f"Bearer {self.openrouter_api_key}",
#             "Content-Type": "application/json",
#             "HTTP-Referer": "http://localhost:8000" # Replace with your actual app URL
#         }
#         payload = {
#             "model": self.openrouter_embedding_model_name,
#             "input": text,
#         }

#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.post(self.openrouter_api_base, headers=headers, json=payload, timeout=30.0)
#                 response.raise_for_status() # Raise an exception for 4xx or 5xx status codes

#                 data = response.json()
#                 if data and 'data' in data and len(data['data']) > 0 and 'embedding' in data['data'][0]:
#                     return data['data'][0]['embedding']
#                 else:
#                     print(f"OpenRouter API response missing embedding data: {data}")
#                     return None
#             except httpx.RequestError as e:
#                 print(f"An error occurred while requesting OpenRouter API: {e}")
#                 return None
#             except httpx.HTTPStatusError as e:
#                 print(f"OpenRouter API returned an error: {e.response.status_code} - {e.response.text}")
#                 return None
#             except Exception as e:
#                 print(f"An unexpected error occurred: {e}")
#                 return None
    
#     def get_embedding_model_name(self) -> str:
#         """Returns the name of the embedding model being used."""
#         return self.openrouter_embedding_model_name




# import httpx
# from typing import List, Optional
# from ..core.config import get_settings

# class EmbeddingService:
#     def __init__(self):
#         self.settings = get_settings()
#         self.api_key = self.settings.OPENROUTER_API_KEY
#         self.model_name = self.settings.OPENROUTER_EMBEDDING_MODEL_NAME
#         self.api_base = "https://openrouter.ai/api/v1/embeddings"

#     async def generate_embedding(self, text: str) -> Optional[List[float]]:
#         """
#         Generates an embedding for the given text using OpenRouter API.
#         Returns a list of floats or None if error occurs.
#         """
#         headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json",
#             "HTTP-Referer": "http://localhost:8000"  # Update if using production URL
#         }
#         payload = {
#             "model": self.model_name,
#             "input": text,
#         }

#         async with httpx.AsyncClient() as client:
#             try:
#                 response = await client.post(self.api_base, headers=headers, json=payload, timeout=30.0)
#                 response.raise_for_status()

#                 data = response.json()
#                 if "data" in data and len(data["data"]) > 0 and "embedding" in data["data"][0]:
#                     return data["data"][0]["embedding"]
#                 else:
#                     print(f"[EmbeddingService] Missing embedding in response: {data}")
#                     return None

#             except httpx.RequestError as e:
#                 print(f"[EmbeddingService] Request error: {e}")
#                 return None
#             except httpx.HTTPStatusError as e:
#                 print(f"[EmbeddingService] HTTP error {e.response.status_code}: {e.response.text}")
#                 return None
#             except Exception as e:
#                 print(f"[EmbeddingService] Unexpected error: {e}")
#                 return None

#     def get_embedding_model_name(self) -> str:
#         """Return the embedding model name."""
#         return self.model_name



import httpx
from typing import List, Optional
import logging
from ..core.config import get_settings

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self):
        self.settings = get_settings()
        self.api_key = self.settings.OPENROUTER_API_KEY
        self.model_name = self.settings.OPENROUTER_EMBEDDING_MODEL_NAME
        self.api_base = "https://openrouter.ai/api/v1/embeddings"

    async def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        Generates an embedding for the given text using OpenRouter API.
        Returns a list of floats, or None if there is an error.
        """
        if not text.strip():
            logger.warning("Empty text provided for embedding.")
            return None

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000"
        }

        payload = {
            "model": self.model_name,
            "input": text,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.api_base, headers=headers, json=payload, timeout=30.0)
                response.raise_for_status()
                data = response.json()

                if "data" in data and len(data["data"]) > 0 and "embedding" in data["data"][0]:
                    logger.info("Successfully generated embedding.")
                    return data["data"][0]["embedding"]
                else:
                    logger.error(f"Embedding generation failed: returned None. Response data: {data}")
                    return None

            except httpx.RequestError as e:
                logger.error(f"OpenRouter API request error: {e}", exc_info=True)
                return None
            except httpx.HTTPStatusError as e:
                logger.error(f"OpenRouter API HTTP error {e.response.status_code}: {e.response.text}", exc_info=True)
                return None
            except Exception as e:
                logger.error(f"An unexpected error occurred during embedding generation: {e}", exc_info=True)
                return None

    def get_embedding_model_name(self) -> str:
        """Return the embedding model name."""
        return self.model_name
