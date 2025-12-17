# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# from .api.api_router import router as api_router

# from backend.src.services.qdrant_service import QdrantService
# from backend.src.services.neon_service import NeonService
# from backend.src.services.embedding_service import EmbeddingService
# from backend.src.services.chunking_service import ChunkingService
# from backend.src.services.indexing_service import IndexingService

# # Define application lifespan events (startup/shutdown)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup logic: e.g., connect to databases, load models
#     print("FastAPI application starting up...")
    
#     # Instantiate services
#     qdrant_service = QdrantService()
#     neon_service = NeonService()
#     embedding_service = EmbeddingService()
#     chunking_service = ChunkingService()
    
#     # Instantiate IndexingService and attach to app state
#     # Assuming book_content_dir and specify_txt_path are configured somewhere, e.g., in config
#     app.state.indexing_service = IndexingService(
#         qdrant_service=qdrant_service,
#         neon_service=neon_service,
#         embedding_service=embedding_service,
#         chunking_service=chunking_service,
#         book_content_dir="book_source/docs", # Hardcoded for now
#         specify_txt_path="specify.txt" # Hardcoded for now
#     )

#     yield # Application runs
    
#     # Shutdown logic: e.g., close database connections
#     print("FastAPI application shutting down...")

# app = FastAPI(
#     title="RAG Chatbot API",
#     description="API for the Retrieval Augmented Generation (RAG) Chatbot for Docusaurus Book.",
#     version="1.0.0",
#     lifespan=lifespan
# )

# @app.get("/")
# async def read_root():
#     return {"message": "RAG Chatbot API is running!"}

# # Include API routers here as they are developed
# app.include_router(api_router)



# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# from .api.api_router import router as api_router

# from backend.src.services.qdrant_service import QdrantService
# from backend.src.services.neon_service import NeonService
# from backend.src.services.embedding_service import EmbeddingService
# from backend.src.services.chunking_service import ChunkingService
# from backend.src.services.indexing_service import IndexingService


# # Define application lifespan events (startup/shutdown)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup logic
#     print("FastAPI application starting up...")

#     # Instantiate services
#     qdrant_service = QdrantService()
#     neon_service = NeonService()
#     embedding_service = EmbeddingService()
#     chunking_service = ChunkingService()


#     # Instantiate IndexingService and attach
#     app.state.indexing_service = IndexingService(
#         qdrant_service=qdrant_service,
#         neon_service=neon_service,
#         embedding_service=embedding_service,
#         chunking_service=chunking_service,
#         book_content_dir="book_source/docs",  # Path to your book docs
#         specify_txt_path="specify.txt"        # Path to specify.txt
#     )

#     yield  # Application runs

#     # Shutdown logic
#     print("FastAPI application shutting down...")


# # Create FastAPI app with lifespan
# app = FastAPI(
#     title="RAG Chatbot API",
#     description="API for the Retrieval Augmented Generation (RAG) Chatbot for Docusaurus Book.",
#     version="1.0.0",
#     lifespan=lifespan
# )

# # Root endpoint
# @app.get("/")
# async def read_root():
#     return {"message": "RAG Chatbot API is running!"}

# # Include API router for /chat and /index-book
# app.include_router(api_router)










import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .api.api_router import router as api_router
from fastapi.middleware.cors import CORSMiddleware

from backend.src.services.qdrant_service import QdrantService
from backend.src.services.neon_service import NeonService
from backend.src.services.embedding_service import EmbeddingService
from backend.src.services.chunking_service import ChunkingService
from backend.src.services.indexing_service import IndexingService
from backend.src.services.gemini_service import GeminiService

# Configure logging at the application's entry point
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# --- Define application lifespan events (startup/shutdown) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("FastAPI application starting up...")

    # Instantiate individual services
    qdrant_service = QdrantService()
    neon_service = NeonService()
    embedding_service = EmbeddingService()
    chunking_service = ChunkingService()
    gemini_service = GeminiService()

    # Attach services to app.state so endpoints can access them
    app.state.qdrant_service = qdrant_service
    app.state.embedding_service = embedding_service
    app.state.neon_service = neon_service
    app.state.chunking_service = chunking_service
    app.state.gemini_service = gemini_service

    # Instantiate IndexingService and attach
    app.state.indexing_service = IndexingService(
        qdrant_service=qdrant_service,
        neon_service=neon_service,
        embedding_service=embedding_service,
        chunking_service=chunking_service,
        book_content_dir="book_source/docs",
        specify_txt_path="specify.txt"
    )

    yield  # Application runs

    # Shutdown logic
    logging.info("FastAPI application shutting down...")

# --- Create FastAPI app ---
app = FastAPI(
    title="RAG Chatbot API",
    description="API for the Retrieval Augmented Generation (RAG) Chatbot for Docusaurus Book.",
    version="1.0.0",
    lifespan=lifespan
)

# --- Add CORS middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# --- Root endpoint ---
@app.get("/")
async def read_root():
    return {"message": "RAG Chatbot API is running!"}

# --- Include API router for /chat and /index-book ---
app.include_router(api_router)
