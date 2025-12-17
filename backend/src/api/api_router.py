

#     try:
#         # 1. Generate embedding for query
#         query_embedding = embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # 2. Retrieve chunks from Qdrant
#         # For selected_text context, retrieval should be filtered. (T041)
#         # For now, always search full book
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question from the provided content.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # 3. Generate answer using Gemini
#         answer = gemini_service.generate_answer(query.query, retrieved_chunks)

#         end_time = time.time()
#         response_time_ms = (end_time - start_time) * 1000

#         # T037: Implement logic to display answers with source text in the API response
#         # The ChatbotResponse model already includes source_chunks
#         return ChatbotResponse(
#             answer=answer,
#             source_chunks=retrieved_chunks,
#             response_time_ms=response_time_ms
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")






#     try:
#         # 1. Generate embedding for query
#         query_embedding = embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # 2. Retrieve chunks from Qdrant
#         # For selected_text context, retrieval should be filtered. (T041)
#         # For now, always search full book
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question from the provided content.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # 3. Generate answer using Gemini
#         answer = gemini_service.generate_answer(query.query, retrieved_chunks)

#         end_time = time.time()
#         response_time_ms = (end_time - start_time) * 1000

#         # T037: Implement logic to display answers with source text in the API response
#         # The ChatbotResponse model already includes source_chunks
#         return ChatbotResponse(
#             answer=answer,
#             source_chunks=retrieved_chunks,
#             response_time_ms=response_time_ms
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")









# from fastapi import APIRouter, HTTPException, Depends, Request
# import time  # For response_time_ms
# from typing import List, Optional
# from ..models.data_models import (
#     UserQuery,
#     ChatbotResponse,
#     IndexBookRequest,
#     IndexBookResponse,
#     Chunk
# )
# from ..services.indexing_service import IndexingService
# from ..services.embedding_service import EmbeddingService
# from ..services.qdrant_service import QdrantService


# router = APIRouter()

# # --- Dependencies to get services from app state ---
# def get_indexing_service(request: Request) -> IndexingService:
#     return request.app.state.indexing_service

# def get_embedding_service(request: Request) -> EmbeddingService:
#     return request.app.state.embedding_service

# def get_qdrant_service(request: Request) -> QdrantService:
#     return request.app.state.qdrant_service



# # --- Chat endpoint ---
# @router.post("/chat", response_model=ChatbotResponse)
# async def chat_endpoint(
#     query: UserQuery,
#     embedding_service: EmbeddingService = Depends(get_embedding_service),
#     qdrant_service: QdrantService = Depends(get_qdrant_service)
# ):
#     """
#     Handles user queries, retrieves relevant chunks, and generates a response.
#     """
#     start_time = time.time()

#     try:
#         # 1. Generate embedding for query
#         query_embedding = await embedding_service.generate_embedding(query.query) # Added await
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # 2. Retrieve chunks from Qdrant
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question from the provided content.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # 3. Placeholder for answer generation (GeminiService removed)
#         answer = "Chat completion is not available as GeminiService has been removed. Retrieved information:\n\n" + "\n\n".join([f"Source: {c.metadata.file_path}, Page: {c.metadata.page_number}\nText: {c.text}" for c in retrieved_chunks])

#         response_time_ms = (time.time() - start_time) * 1000

#         return ChatbotResponse(
#             answer=answer,
#             source_chunks=retrieved_chunks,
#             response_time_ms=response_time_ms
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# # --- Index-book endpoint ---
# @router.post("/index-book", response_model=IndexBookResponse)
# async def index_book_endpoint(
#     request: Request,
#     indexing_service: IndexingService = Depends(get_indexing_service),
#     payload: Optional[IndexBookRequest] = None
# ):
#     """
#     Trigger indexing of the Docusaurus book content.
#     """
#     force_reindex = False
#     if payload and hasattr(payload, "force"):
#         force_reindex = payload.force

#     indexing_service.run_indexing_process(force_reindex=force_reindex)

#     return IndexBookResponse(message="Indexing triggered successfully!")










# from fastapi import APIRouter, HTTPException, Depends, Request
# import time
# from typing import List, Optional
# from ..models.data_models import UserQuery, ChatbotResponse, IndexBookRequest, IndexBookResponse, Chunk
# from ..services.indexing_service import IndexingService
# from ..services.embedding_service import EmbeddingService
# from ..services.qdrant_service import QdrantService

# router = APIRouter()

# # --- Dependencies ---
# def get_indexing_service(request: Request) -> IndexingService:
#     return request.app.state.indexing_service

# def get_embedding_service(request: Request) -> EmbeddingService:
#     return request.app.state.embedding_service

# def get_qdrant_service(request: Request) -> QdrantService:
#     return request.app.state.qdrant_service

# # --- Chat endpoint ---
# @router.post("/chat", response_model=ChatbotResponse)
# async def chat_endpoint(
#     query: UserQuery,
#     embedding_service: EmbeddingService = Depends(get_embedding_service),
#     qdrant_service: QdrantService = Depends(get_qdrant_service)
# ):
#     start_time = time.time()
#     try:
#         query_embedding = await embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         answer = "Chat completion is not available. Retrieved info:\n\n" + "\n\n".join(
#             [f"Source: {c.metadata.file_path}, Page: {c.metadata.page}\nText: {c.text}" for c in retrieved_chunks]
#         )

#         return ChatbotResponse(
#             answer=answer,
#             source_chunks=retrieved_chunks,
#             response_time_ms=(time.time() - start_time) * 1000
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# # --- Index-book endpoint ---
# @router.post("/index-book", response_model=IndexBookResponse)
# async def index_book_endpoint(
#     request: Request,
#     indexing_service: IndexingService = Depends(get_indexing_service),
#     payload: Optional[IndexBookRequest] = None
# ):
#     force_reindex = getattr(payload, "force", False)
#     await indexing_service.run_indexing_process(force_reindex=force_reindex)
#     return IndexBookResponse(message="Indexing completed successfully!")








# from fastapi import APIRouter, HTTPException, Depends, Request
# import time
# from typing import List, Optional
# from ..models.data_models import UserQuery, ChatbotResponse, IndexBookRequest, IndexBookResponse, Chunk
# from ..services.indexing_service import IndexingService
# from ..services.embedding_service import EmbeddingService
# from ..services.qdrant_service import QdrantService

# router = APIRouter()

# # --- Dependencies ---
# def get_indexing_service(request: Request) -> IndexingService:
#     """Retrieve indexing service from app state."""
#     if not hasattr(request.app.state, "indexing_service"):
#         raise HTTPException(status_code=500, detail="Indexing service not initialized.")
#     return request.app.state.indexing_service

# def get_embedding_service(request: Request) -> EmbeddingService:
#     """Retrieve embedding service from app state."""
#     if not hasattr(request.app.state, "embedding_service"):
#         raise HTTPException(status_code=500, detail="Embedding service not initialized.")
#     return request.app.state.embedding_service

# def get_qdrant_service(request: Request) -> QdrantService:
#     """Retrieve Qdrant service from app state."""
#     if not hasattr(request.app.state, "qdrant_service"):
#         raise HTTPException(status_code=500, detail="Qdrant service not initialized.")
#     return request.app.state.qdrant_service

# # --- Chat endpoint ---
# @router.post("/chat", response_model=ChatbotResponse)
# async def chat_endpoint(
#     query: UserQuery,
#     embedding_service: EmbeddingService = Depends(get_embedding_service),
#     qdrant_service: QdrantService = Depends(get_qdrant_service)
# ):
#     start_time = time.time()
#     try:
#         # Generate embedding for the user query
#         query_embedding = await embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # Retrieve relevant chunks from Qdrant
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         # If no relevant info found
#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # Combine retrieved chunks into answer
#         answer = "Chat completion is not available. Retrieved info:\n\n" + "\n\n".join(
#             [f"Source: {c.metadata.file_path}, Page: {c.metadata.page}\nText: {c.text}" for c in retrieved_chunks]
#         )

#         return ChatbotResponse(
#             answer=answer,
#             source_chunks=retrieved_chunks,
#             response_time_ms=(time.time() - start_time) * 1000
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# # --- Index-book endpoint ---
# @router.post("/index-book", response_model=IndexBookResponse)
# async def index_book_endpoint(
#     request: Request,
#     indexing_service: IndexingService = Depends(get_indexing_service),
#     payload: Optional[IndexBookRequest] = None
# ):
#     force_reindex = getattr(payload, "force", False)
#     try:
#         await indexing_service.run_indexing_process(force_reindex=force_reindex)
#         return IndexBookResponse(message="Indexing completed successfully!")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")










# from fastapi import APIRouter, HTTPException, Depends, Request
# import time
# from typing import List, Optional
# from ..models.data_models import UserQuery, ChatbotResponse, IndexBookRequest, IndexBookResponse, Chunk
# from ..services.indexing_service import IndexingService
# from ..services.embedding_service import EmbeddingService
# from ..services.qdrant_service import QdrantService
# import traceback

# router = APIRouter()

# # --- Dependencies ---
# def get_indexing_service(request: Request) -> IndexingService:
#     if not hasattr(request.app.state, "indexing_service"):
#         raise HTTPException(status_code=500, detail="Indexing service not initialized.")
#     return request.app.state.indexing_service

# def get_embedding_service(request: Request) -> EmbeddingService:
#     if not hasattr(request.app.state, "embedding_service"):
#         raise HTTPException(status_code=500, detail="Embedding service not initialized.")
#     return request.app.state.embedding_service

# def get_qdrant_service(request: Request) -> QdrantService:
#     if not hasattr(request.app.state, "qdrant_service"):
#         raise HTTPException(status_code=500, detail="Qdrant service not initialized.")
#     return request.app.state.qdrant_service

# # --- Chat endpoint ---
# @router.post("/chat", response_model=ChatbotResponse)
# async def chat_endpoint(
#     query: UserQuery,
#     embedding_service: EmbeddingService = Depends(get_embedding_service),
#     qdrant_service: QdrantService = Depends(get_qdrant_service)
# ):
#     start_time = time.time()
#     try:
#         # Validate query
#         if not query.query or not query.query.strip():
#             raise HTTPException(status_code=400, detail="Query cannot be empty.")

#         # Generate embedding
#         query_embedding = await embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # Retrieve chunks
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         # If nothing found
#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # Combine chunks into answer
#         answer_text = "Chat completion not available. Retrieved info:\n\n" + "\n\n".join(
#             [f"Source: {c.metadata.file_path}, Page: {c.metadata.page}\nText: {c.text}" for c in retrieved_chunks]
#         )

#         return ChatbotResponse(
#             answer=answer_text,
#             source_chunks=retrieved_chunks,
#             response_time_ms=(time.time() - start_time) * 1000
#         )

#     except HTTPException:
#         # Re-raise known HTTP exceptions
#         raise
#     except Exception as e:
#         # Print full traceback for debugging
#         print("ERROR in /chat endpoint:")
#         print(traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# # --- Index-book endpoint ---
# @router.post("/index-book", response_model=IndexBookResponse)
# async def index_book_endpoint(
#     request: Request,
#     indexing_service: IndexingService = Depends(get_indexing_service),
#     payload: Optional[IndexBookRequest] = None
# ):
#     force_reindex = getattr(payload, "force", False) if payload else False
#     try:
#         await indexing_service.run_indexing_process(force_reindex=force_reindex)
#         return IndexBookResponse(message="Indexing completed successfully!")
#     except Exception as e:
#         print("ERROR in /index-book endpoint:")
#         print(traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")




# from fastapi import APIRouter, HTTPException, Depends, Request
# import time
# from typing import List, Optional
# from ..models.data_models import UserQuery, ChatbotResponse, IndexBookRequest, IndexBookResponse, Chunk
# from ..services.indexing_service import IndexingService
# from ..services.embedding_service import EmbeddingService
# from ..services.qdrant_service import QdrantService
# import traceback

# router = APIRouter()

# # --- Dependencies ---
# def get_indexing_service(request: Request) -> IndexingService:
#     if not hasattr(request.app.state, "indexing_service"):
#         raise HTTPException(status_code=500, detail="Indexing service not initialized.")
#     return request.app.state.indexing_service

# def get_embedding_service(request: Request) -> EmbeddingService:
#     if not hasattr(request.app.state, "embedding_service"):
#         raise HTTPException(status_code=500, detail="Embedding service not initialized.")
#     return request.app.state.embedding_service

# def get_qdrant_service(request: Request) -> QdrantService:
#     if not hasattr(request.app.state, "qdrant_service"):
#         raise HTTPException(status_code=500, detail="Qdrant service not initialized.")
#     return request.app.state.qdrant_service

# # --- Chat endpoint ---
# @router.post("/chat", response_model=ChatbotResponse)
# async def chat_endpoint(
#     query: UserQuery,
#     embedding_service: EmbeddingService = Depends(get_embedding_service),
#     qdrant_service: QdrantService = Depends(get_qdrant_service)
# ):
#     start_time = time.time()
#     try:
#         if not query.query or not query.query.strip():
#             raise HTTPException(status_code=400, detail="Query cannot be empty.")

#         # Generate embedding
#         query_embedding = await embedding_service.generate_embedding(query.query)
#         if not query_embedding:
#             raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

#         # Retrieve chunks
#         retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

#         # Filter out empty text chunks
#         retrieved_chunks = [c for c in retrieved_chunks if c.text.strip()]
        
#         if not retrieved_chunks:
#             return ChatbotResponse(
#                 answer="I don't have enough information to answer that question.",
#                 source_chunks=[],
#                 response_time_ms=(time.time() - start_time) * 1000
#             )

#         # Build answer from chunks
#         answer_text = "\n\n".join(
#             [f"Source: {c.metadata.file_path or 'Unknown'}, Page: {c.metadata.page or 'N/A'}\nText: {c.text}" for c in retrieved_chunks]
#         )

#         return ChatbotResponse(
#             answer=answer_text,
#             source_chunks=retrieved_chunks,
#             response_time_ms=(time.time() - start_time) * 1000
#         )

#     except HTTPException:
#         raise
#     except Exception as e:
#         print("ERROR in /chat endpoint:")
#         print(traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# # --- Index-book endpoint ---
# @router.post("/index-book", response_model=IndexBookResponse)
# async def index_book_endpoint(
#     request: Request,
#     indexing_service: IndexingService = Depends(get_indexing_service),
#     payload: Optional[IndexBookRequest] = None
# ):
#     force_reindex = getattr(payload, "force", False) if payload else False
#     try:
#         await indexing_service.run_indexing_process(force_reindex=force_reindex)
#         return IndexBookResponse(message="Indexing completed successfully!")
#     except Exception as e:
#         print("ERROR in /index-book endpoint:")
#         print(traceback.format_exc())
#         raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")
































# backend/src/api/api_router.py

from fastapi import APIRouter, HTTPException, Depends, Request
import time
from typing import List, Optional
from ..models.data_models import UserQuery, ChatbotResponse, IndexBookRequest, IndexBookResponse, Chunk
from ..services.indexing_service import IndexingService
from ..services.embedding_service import EmbeddingService
from ..services.qdrant_service import QdrantService
from ..services.gemini_service import GeminiService
import traceback

router = APIRouter()

# --- Dependencies ---
def get_indexing_service(request: Request) -> IndexingService:
    if not hasattr(request.app.state, "indexing_service"):
        raise HTTPException(status_code=500, detail="Indexing service not initialized.")
    return request.app.state.indexing_service

def get_embedding_service(request: Request) -> EmbeddingService:
    if not hasattr(request.app.state, "embedding_service"):
        raise HTTPException(status_code=500, detail="Embedding service not initialized.")
    return request.app.state.embedding_service

def get_qdrant_service(request: Request) -> QdrantService:
    if not hasattr(request.app.state, "qdrant_service"):
        raise HTTPException(status_code=500, detail="Qdrant service not initialized.")
    return request.app.state.qdrant_service

def get_gemini_service(request: Request) -> GeminiService:
    if not hasattr(request.app.state, "gemini_service"):
        raise HTTPException(status_code=500, detail="Gemini service not initialized.")
    return request.app.state.gemini_service

# --- Chat endpoint ---
@router.post("/chat", response_model=ChatbotResponse)
async def chat_endpoint(
    query: UserQuery,
    embedding_service: EmbeddingService = Depends(get_embedding_service),
    qdrant_service: QdrantService = Depends(get_qdrant_service),
    gemini_service: GeminiService = Depends(get_gemini_service)
):
    start_time = time.time()
    try:
        if not query.query or not query.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty.")

        # Generate embedding
        query_embedding = await embedding_service.generate_embedding(query.query)
        if not query_embedding:
            raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

        # Retrieve chunks from Qdrant
        retrieved_chunks: List[Chunk] = qdrant_service.search_chunks(query_embedding, limit=5)

        # --- Filter out empty text chunks and ensure metadata ---
        filtered_chunks = []
        for chunk in retrieved_chunks:
            if chunk.text and chunk.text.strip():
                if not chunk.metadata.file_path:
                    chunk.metadata.file_path = "Unknown"
                if chunk.metadata.page is None:
                    chunk.metadata.page = "N/A"
                filtered_chunks.append(chunk)

        if not filtered_chunks:
            return ChatbotResponse(
                answer="I don't have enough information to answer that question.",
                source_chunks=[],
                response_time_ms=(time.time() - start_time) * 1000
            )

        # Generate answer using Gemini
        answer_text = gemini_service.generate_answer(query.query, filtered_chunks)

        return ChatbotResponse(
            answer=answer_text,
            source_chunks=filtered_chunks,
            response_time_ms=(time.time() - start_time) * 1000
        )

    except HTTPException:
        raise
    except Exception as e:
        print("ERROR in /chat endpoint:")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Chatbot query failed: {str(e)}")

# --- Index-book endpoint ---
@router.post("/index-book", response_model=IndexBookResponse)
async def index_book_endpoint(
    request: Request,
    indexing_service: IndexingService = Depends(get_indexing_service),
    payload: Optional[IndexBookRequest] = None
):
    force_reindex = getattr(payload, "force", False) if payload else False
    try:
        await indexing_service.run_indexing_process(force_reindex=force_reindex)
        return IndexBookResponse(message="Indexing completed successfully!")
    except Exception as e:
        print("ERROR in /index-book endpoint:")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")
