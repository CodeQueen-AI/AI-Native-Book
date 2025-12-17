# from pydantic import BaseModel, Field
# from typing import List, Optional, Dict, Any
# from datetime import datetime

# # --- Entities from data-model.md ---

# class DocusaurusBookContent(BaseModel):
#     file_path: str
#     content: str

# class ChunkMetadata(BaseModel):
#     heading: Optional[str] = None
#     page: Optional[int] = None
#     index: Optional[int] = None
#     file_path: str

# class Chunk(BaseModel):
#     id: str
#     text: str
#     metadata: ChunkMetadata
#     embedding: Optional[List[float]] = None # Will be populated after embedding generation

# class Embedding(BaseModel):
#     vector: List[float]
#     model_id: str

# class UserQuery(BaseModel):
#     query: str
#     context_type: str # "full_book" or "selected_text"
#     selected_text: Optional[str] = None

# class ChatbotResponse(BaseModel):
#     answer: str
#     source_chunks: List[Chunk] # Simplified to include full chunk for now
#     response_time_ms: float

# # --- Additional models for internal use or API ---

# class IndexBookRequest(BaseModel):
#     force: bool = False

# class IndexBookResponse(BaseModel):
#     message: str




from pydantic import BaseModel
from typing import List, Optional

# --- Entities from data-model.md ---

class DocusaurusBookContent(BaseModel):
    file_path: str
    content: str

class ChunkMetadata(BaseModel):
    heading: Optional[str] = None
    page: Optional[int] = None
    index: Optional[int] = None
    file_path: str = ""  # default empty to prevent missing errors

class Chunk(BaseModel):
    id: str
    text: str  # MUST NOT BE EMPTY for proper retrieval
    metadata: ChunkMetadata
    embedding: Optional[List[float]] = None  # Populated after embedding generation

class Embedding(BaseModel):
    vector: List[float]
    model_id: str

class UserQuery(BaseModel):
    query: str
    context_type: str  # "full_book" or "selected_text"
    selected_text: Optional[str] = None

class ChatbotResponse(BaseModel):
    answer: str
    source_chunks: List[Chunk]  # Full chunks included
    response_time_ms: float

# --- Additional models for internal use or API ---

class IndexBookRequest(BaseModel):
    force: bool = False

class IndexBookResponse(BaseModel):
    message: str
