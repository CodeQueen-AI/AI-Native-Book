# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse
# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata
# from typing import List

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Deletes and recreates the Qdrant collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Collection '{self.collection_name}' deleted.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e): # Collection might not exist
#                 print(f"Collection '{self.collection_name}' not found, proceeding to create.")
#             else:
#                 raise e # Re-raise if it's another error

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Collection '{self.collection_name}' recreated with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upserts a list of chunks into the Qdrant collection."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding, skipping upsert.")
#                 continue
            
#             # Convert ChunkMetadata to dict for payload
#             payload = chunk.metadata.model_dump() if isinstance(chunk.metadata, ChunkMetadata) else chunk.metadata
#             payload["text"] = chunk.text # Store original text in payload as well

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload,
#                 )
#             )
        
#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(self, query_embedding: List[float], limit: int = 5, selected_text_embedding: Optional[List[float]] = None) -> List[Chunk]:
#         """Searches for relevant chunks in the Qdrant collection, optionally re-ranking based on selected text context."""
        
#         # Initial search based on the primary query embedding
#         search_results_query = self.client.search(
#             collection_name=self.collection_name,
#             query_vector=query_embedding,
#             limit=limit,
#             with_payload=True,
#             with_vectors=False,
#         )

#         combined_results_map: Dict[str, ScoredPoint] = {}
#         for hit in search_results_query:
#             combined_results_map[str(hit.id)] = hit
        
#         # If selected_text_embedding is provided, perform another search and combine/re-rank
#         if selected_text_embedding:
#             search_results_selected_text = self.client.search(
#                 collection_name=self.collection_name,
#                 query_vector=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True,
#                 with_vectors=False,
#             )
#             # A simple combination strategy: add selected_text results,
#             # potentially re-ranking by sum of scores or using a more sophisticated algorithm.
#             # For now, we'll just ensure unique results and potentially extend.
#             for hit in search_results_selected_text:
#                 if str(hit.id) not in combined_results_map:
#                     combined_results_map[str(hit.id)] = hit
#                 else:
#                     # If already present, consider combining scores or taking the max score
#                     # For simplicity, we keep the one already there, or update if score is higher
#                     if hit.score > combined_results_map[str(hit.id)].score:
#                          combined_results_map[str(hit.id)] = hit

#         # Sort the combined results by score (descending)
#         sorted_results = sorted(combined_results_map.values(), key=lambda x: x.score, reverse=True)[:limit]

#         found_chunks = []
#         for hit in sorted_results:
#             payload = hit.payload if hit.payload else {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(**{k: v for k, v in payload.items() if k != "text"}),
#                     embedding=None
#                 )
#             )
#         return found_chunks














# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse
# from qdrant_client.models import ScoredPoint

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Deletes and recreates the Qdrant collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Collection '{self.collection_name}' deleted.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):  # Collection might not exist
#                 print(f"Collection '{self.collection_name}' not found, proceeding to create.")
#             else:
#                 raise e  # Re-raise if it's another error

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Collection '{self.collection_name}' recreated with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upserts a list of chunks into the Qdrant collection."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding, skipping upsert.")
#                 continue

#             # Convert ChunkMetadata to dict for payload
#             payload = chunk.metadata.model_dump() if isinstance(chunk.metadata, ChunkMetadata) else chunk.metadata
#             payload["text"] = chunk.text  # Store original text in payload as well

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload,
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Searches for relevant chunks, optionally re-ranking based on selected text embedding."""

#         # --- Primary search ---
#         search_results_query = self.client.search_points(
#             collection_name=self.collection_name,
#             vector=query_embedding,
#             limit=limit,
#             with_payload=True,
#             with_vectors=False,
#         )

#         combined_results_map: Dict[str, ScoredPoint] = {}
#         for hit in search_results_query:
#             combined_results_map[str(hit.id)] = hit

#         # --- Optional re-ranking with selected text ---
#         if selected_text_embedding:
#             search_results_selected_text = self.client.search_points(
#                 collection_name=self.collection_name,
#                 vector=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True,
#                 with_vectors=False,
#             )

#             for hit in search_results_selected_text:
#                 hit_id = str(hit.id)
#                 if hit_id not in combined_results_map:
#                     combined_results_map[hit_id] = hit
#                 else:
#                     if hit.score > combined_results_map[hit_id].score:
#                         combined_results_map[hit_id] = hit

#         # --- Sort & limit ---
#         sorted_results = sorted(
#             combined_results_map.values(),
#             key=lambda x: x.score,
#             reverse=True
#         )[:limit]

#         # --- Convert to Chunk objects ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_results:
#             payload = hit.payload or {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None
#                 )
#             )

#         return found_chunks














# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse
# from qdrant_client.models import ScoredPoint

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Collection '{self.collection_name}' deleted.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, creating.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Collection recreated with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} missing embedding, skipping.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload,
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True,
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None,
#     ) -> List[Chunk]:

#         # --- Primary search using `search()` correct for your installed client ---
#         search_results_query = self.client.search(
#             collection_name=self.collection_name,
#             query_vector=query_embedding,
#             limit=limit,
#             with_payload=True,
#             with_vectors=False,
#         )

#         combined_results_map: Dict[str, ScoredPoint] = {}
#         for hit in search_results_query:
#             combined_results_map[str(hit.id)] = hit

#         # --- Optional re-ranking if provided ---
#         if selected_text_embedding:
#             search_results_selected_text = self.client.search(
#                 collection_name=self.collection_name,
#                 query_vector=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True,
#                 with_vectors=False,
#             )

#             for hit in search_results_selected_text:
#                 hit_id = str(hit.id)
#                 if hit_id not in combined_results_map:
#                     combined_results_map[hit_id] = hit
#                 else:
#                     if hit.score > combined_results_map[hit_id].score:
#                         combined_results_map[hit_id] = hit

#         # --- Sort and trim ---
#         sorted_results = sorted(
#             combined_results_map.values(),
#             key=lambda x: x.score,
#             reverse=True,
#         )[:limit]

#         # --- Build results ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_results:
#             payload = hit.payload or {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None,
#                 )
#             )

#         return found_chunks


















# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Deletes and recreates the Qdrant collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Collection '{self.collection_name}' deleted.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, proceeding to create.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Collection '{self.collection_name}' recreated with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upserts a list of chunks into the Qdrant collection."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding, skipping upsert.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload,
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True,
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Searches for relevant chunks in the Qdrant collection."""

#         # --- Primary search (compatible with your installed client) ---
#         search_results_query = self.client.search(
#             collection_name=self.collection_name,
#             vector=query_embedding,  # correct parameter for your client version
#             limit=limit,
#             with_payload=True,
#             with_vector=False,
#         )

#         combined_results_map: Dict[str, any] = {}
#         for hit in search_results_query:
#             combined_results_map[str(hit.id)] = hit

#         # --- Optional re-ranking with selected_text_embedding ---
#         if selected_text_embedding:
#             search_results_selected_text = self.client.search(
#                 collection_name=self.collection_name,
#                 vector=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True,
#                 with_vector=False,
#             )

#             for hit in search_results_selected_text:
#                 hit_id = str(hit.id)
#                 if hit_id not in combined_results_map:
#                     combined_results_map[hit_id] = hit
#                 else:
#                     if hit.score > combined_results_map[hit_id].score:
#                         combined_results_map[hit_id] = hit

#         # --- Sort by score descending ---
#         sorted_results = sorted(
#             combined_results_map.values(),
#             key=lambda x: x.score,
#             reverse=True
#         )[:limit]

#         # --- Convert to Chunk objects ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_results:
#             payload = hit.payload or {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None
#                 )
#             )

#         return found_chunks




































# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Delete and recreate the collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Deleted collection '{self.collection_name}'.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, creating it.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Recreated '{self.collection_name}' with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upsert chunks to Qdrant."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding — skipping.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Search for similar chunks in Qdrant using `query_points()`."""

#         # --- Primary vector search ---
#         response_query = self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_embedding,
#             limit=limit,
#             with_payload=True,
#             with_vector=False
#         )

#         combined_results: Dict[str, any] = {}
#         for hit in response_query:
#             combined_results[str(hit.id)] = hit

#         # --- Optional second search for selected_text_embedding ---
#         if selected_text_embedding:
#             response_selected = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True,
#                 with_vector=False
#             )
#             for hit in response_selected:
#                 hit_id = str(hit.id)
#                 if hit_id not in combined_results:
#                     combined_results[hit_id] = hit
#                 else:
#                     if hit.score > combined_results[hit_id].score:
#                         combined_results[hit_id] = hit

#         # --- Sort by score descending and limit ---
#         sorted_hits = sorted(
#             combined_results.values(),
#             key=lambda x: x.score,
#             reverse=True
#         )[:limit]

#         found_chunks: List[Chunk] = []
#         for hit in sorted_hits:
#             payload = hit.payload or {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None
#                 )
#             )

#         return found_chunks

























# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Delete and recreate the collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Deleted collection '{self.collection_name}'.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, creating it.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Recreated '{self.collection_name}' with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upsert chunks to Qdrant."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding — skipping.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Search for similar chunks in Qdrant using query_points()."""

#         # --- Primary vector search ---
#         response_query = self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_embedding,
#             limit=limit,
#             with_payload=True
#         )

#         combined_results: Dict[str, any] = {}
#         for hit in response_query:
#             combined_results[str(hit.id)] = hit

#         # --- Optional second search for selected_text_embedding ---
#         if selected_text_embedding:
#             response_selected = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True
#             )
#             for hit in response_selected:
#                 hit_id = str(hit.id)
#                 if hit_id not in combined_results:
#                     combined_results[hit_id] = hit
#                 else:
#                     if hit.score > combined_results[hit_id].score:
#                         combined_results[hit_id] = hit

#         # --- Sort by score descending and limit ---
#         sorted_hits = sorted(
#             combined_results.values(),
#             key=lambda x: x.score,
#             reverse=True
#         )[:limit]

#         # --- Convert to Chunk objects ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_hits:
#             payload = hit.payload or {}
#             found_chunks.append(
#                 Chunk(
#                     id=str(hit.id),
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None
#                 )
#             )

#         return found_chunks

























# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Delete and recreate the collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Deleted collection '{self.collection_name}'.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, creating it.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Recreated '{self.collection_name}' with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upsert chunks to Qdrant."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding — skipping.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Search for similar chunks in Qdrant using query_points() and handle tuple response."""

#         def _process_response(response) -> Dict[str, Dict]:
#             """Convert tuple response to dict with id, score, payload."""
#             results = {}
#             for hit in response:
#                 # Qdrant returns tuple: (id, score, payload)
#                 point_id = str(hit[0])
#                 score = hit[1]
#                 payload = hit[2] if len(hit) > 2 else {}
#                 results[point_id] = {"id": point_id, "score": score, "payload": payload}
#             return results

#         # --- Primary search ---
#         response_query = self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_embedding,
#             limit=limit,
#             with_payload=True
#         )
#         combined_results = _process_response(response_query)

#         # --- Optional re-ranking with selected_text_embedding ---
#         if selected_text_embedding:
#             response_selected = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True
#             )
#             selected_results = _process_response(response_selected)
#             for pid, data in selected_results.items():
#                 if pid not in combined_results:
#                     combined_results[pid] = data
#                 else:
#                     if data["score"] > combined_results[pid]["score"]:
#                         combined_results[pid] = data

#         # --- Sort by score descending ---
#         sorted_hits = sorted(
#             combined_results.values(),
#             key=lambda x: x["score"],
#             reverse=True
#         )[:limit]

#         # --- Convert to Chunk objects ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_hits:
#             payload = hit["payload"] or {}
#             found_chunks.append(
#                 Chunk(
#                     id=hit["id"],
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(
#                         **{k: v for k, v in payload.items() if k != "text"}
#                     ),
#                     embedding=None
#                 )
#             )

#         return found_chunks
























# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         """Delete and recreate the collection."""
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             print(f"Deleted collection '{self.collection_name}'.")
#         except UnexpectedResponse as e:
#             if "not found" in str(e):
#                 print(f"Collection '{self.collection_name}' not found, creating it.")
#             else:
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         print(f"Recreated '{self.collection_name}' with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upsert chunks to Qdrant."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 print(f"Warning: Chunk {chunk.id} has no embedding — skipping.")
#                 continue

#             payload = (
#                 chunk.metadata.model_dump()
#                 if isinstance(chunk.metadata, ChunkMetadata)
#                 else chunk.metadata
#             )
#             payload["text"] = chunk.text

#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )

#         if points:
#             self.client.upsert(
#                 collection_name=self.collection_name,
#                 points=points,
#                 wait=True
#             )
#             print(f"Upserted {len(points)} chunks into '{self.collection_name}'.")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Search for similar chunks in Qdrant using query_points() and handle tuple response."""

#         def _process_response(response) -> Dict[str, Dict]:
#             """Convert tuple response to dict with id, score, payload."""
#             results = {}
#             for hit in response:
#                 # Qdrant returns tuple: (id, score, payload)
#                 point_id = str(hit[0])
#                 score = hit[1]
#                 payload = hit[2] if len(hit) > 2 else {}
#                 results[point_id] = {"id": point_id, "score": score, "payload": payload}
#             return results

#         # --- Primary search ---
#         response_query = self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_embedding,
#             limit=limit,
#             with_payload=True
#         )
#         combined_results = _process_response(response_query)

#         # --- Optional re-ranking with selected_text_embedding ---
#         if selected_text_embedding:
#             response_selected = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True
#             )
#             selected_results = _process_response(response_selected)
#             for pid, data in selected_results.items():
#                 if pid not in combined_results:
#                     combined_results[pid] = data
#                 else:
#                     if data["score"] > combined_results[pid]["score"]:
#                         combined_results[pid] = data

#         # --- Sort by score descending ---
#         sorted_hits = sorted(
#             combined_results.values(),
#             key=lambda x: x["score"],
#             reverse=True
#         )[:limit]

#         # --- Convert to Chunk objects and handle missing required metadata ---
#         found_chunks: List[Chunk] = []
#         for hit in sorted_hits:
#             payload = hit["payload"] or {}
#             metadata_fields = {k: v for k, v in payload.items() if k != "text"}

#             # Fill required fields with defaults if missing
#             if "file_path" not in metadata_fields:
#                 metadata_fields["file_path"] = ""

#             found_chunks.append(
#                 Chunk(
#                     id=hit["id"],
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(**metadata_fields),
#                     embedding=None
#                 )
#             )

#         return found_chunks













# # services/qdrant_service.py
# from typing import List, Optional, Dict
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         self.collection_name = "docusaurus_chunks"

#     def recreate_collection(self, vector_size: int):
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#         except UnexpectedResponse as e:
#             if "not found" not in str(e):
#                 raise e

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )

#     def upsert_chunks(self, chunks: List[Chunk]):
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding:
#                 continue
#             payload = chunk.metadata.model_dump() if isinstance(chunk.metadata, ChunkMetadata) else chunk.metadata
#             payload["text"] = chunk.text
#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )
#         if points:
#             self.client.upsert(collection_name=self.collection_name, points=points, wait=True)

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:

#         def _process_response(response) -> Dict[str, Dict]:
#             results = {}
#             for hit in response:
#                 point_id = str(hit[0])
#                 score = hit[1]
#                 payload = hit[2] if len(hit) > 2 else {}
#                 results[point_id] = {"id": point_id, "score": score, "payload": payload}
#             return results

#         response_query = self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_embedding,
#             limit=limit,
#             with_payload=True
#         )
#         combined_results = _process_response(response_query)

#         if selected_text_embedding:
#             response_selected = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=selected_text_embedding,
#                 limit=limit,
#                 with_payload=True
#             )
#             selected_results = _process_response(response_selected)
#             for pid, data in selected_results.items():
#                 if pid not in combined_results or data["score"] > combined_results[pid]["score"]:
#                     combined_results[pid] = data

#         sorted_hits = sorted(combined_results.values(), key=lambda x: x["score"], reverse=True)[:limit]

#         found_chunks: List[Chunk] = []
#         for hit in sorted_hits:
#             payload = hit["payload"] or {}
#             metadata_fields = {k: v for k, v in payload.items() if k != "text"}
#             if "file_path" not in metadata_fields:
#                 metadata_fields["file_path"] = ""
#             found_chunks.append(
#                 Chunk(
#                     id=hit["id"],
#                     text=payload.get("text", ""),
#                     metadata=ChunkMetadata(**metadata_fields),
#                     embedding=None
#                 )
#             )
#         return found_chunks





















# from typing import List, Optional, Dict
# import logging
# from qdrant_client import QdrantClient, models
# from qdrant_client.http.exceptions import UnexpectedResponse

# from ..core.config import get_settings
# from ..models.data_models import Chunk, ChunkMetadata

# logger = logging.getLogger(__name__)

# class QdrantService:
#     def __init__(self):
#         settings = get_settings()
#         self.client = QdrantClient(
#             url=settings.QDRANT_URL,
#             api_key=settings.QDRANT_API_KEY,
#         )
#         logger.info(f"Qdrant client initialized for remote instance at {settings.QDRANT_URL}")

#     def recreate_collection(self, vector_size: int):
#         """Deletes and recreates the collection."""
#         logger.info(f"Attempting to recreate collection '{self.collection_name}' with vector_size={vector_size} and distance_metric='COSINE'")
#         try:
#             self.client.delete_collection(collection_name=self.collection_name)
#             logger.info(f"Collection '{self.collection_name}' deleted successfully.")
#         except UnexpectedResponse as e:
#             if "not found" not in str(e):
#                 logger.error(f"Error deleting collection '{self.collection_name}': {e}", exc_info=True)
#                 raise e
#             else:
#                 logger.info(f"Collection '{self.collection_name}' not found, proceeding to create.")

#         self.client.recreate_collection(
#             collection_name=self.collection_name,
#             vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
#         )
#         logger.info(f"Collection '{self.collection_name}' recreated successfully with vector size {vector_size}.")

#     def upsert_chunks(self, chunks: List[Chunk]):
#         """Upserts a list of chunks into Qdrant."""
#         points = []
#         for chunk in chunks:
#             if not chunk.embedding or not chunk.text.strip():
#                 logger.warning(f"Skipping chunk {chunk.id} due to missing embedding or empty text. Text: '{chunk.text[:50]}...'")
#                 continue
#             payload = chunk.metadata.model_dump() if isinstance(chunk.metadata, ChunkMetadata) else chunk.metadata
#             payload["text"] = chunk.text
#             points.append(
#                 models.PointStruct(
#                     id=chunk.id,
#                     vector=chunk.embedding,
#                     payload=payload
#                 )
#             )
#         if points:
#             try:
#                 self.client.upsert(collection_name=self.collection_name, points=points, wait=True)
#                 logger.info(f"Successfully upserted {len(points)} chunks into '{self.collection_name}'.")
#             except Exception as e:
#                 logger.error(f"Error during upserting chunks to '{self.collection_name}': {e}", exc_info=True)
#         else:
#             logger.info("No chunks to upsert (empty points list).")

#     def search_chunks(
#         self,
#         query_embedding: List[float],
#         limit: int = 5,
#         selected_text_embedding: Optional[List[float]] = None
#     ) -> List[Chunk]:
#         """Searches for relevant chunks in Qdrant."""
#         logger.info(f"Performing Qdrant search in collection '{self.collection_name}' with limit={limit}.")

#         def _process_response(response) -> Dict[str, Dict]:
#             results = {}
#             for hit in response:
#                 point_id = str(hit[0])
#                 score = hit[1]
#                 payload = hit[2] if len(hit) > 2 else {}
#                 results[point_id] = {"id": point_id, "score": score, "payload": payload}
#             return results

#         try:
#             # Primary search
#             response_query = self.client.query_points(
#                 collection_name=self.collection_name,
#                 query=query_embedding,
#                 limit=limit,
#                 with_payload=True
#             )
#             combined_results = _process_response(response_query)
#             logger.debug(f"Primary search returned {len(response_query)} results.")

#             # Optional re-ranking using selected text
#             if selected_text_embedding:
#                 logger.info("Performing secondary search with selected text embedding for re-ranking.")
#                 response_selected = self.client.query_points(
#                     collection_name=self.collection_name,
#                     query=selected_text_embedding,
#                     limit=limit,
#                     with_payload=True
#                 )
#                 selected_results = _process_response(response_selected)
#                 for pid, data in selected_results.items():
#                     if pid not in combined_results or data["score"] > combined_results[pid]["score"]:
#                         combined_results[pid] = data
#                 logger.debug(f"Secondary search added/updated {len(selected_results)} results.")


#             # Sort and take top results
#             sorted_hits = sorted(combined_results.values(), key=lambda x: x["score"], reverse=True)[:limit]
#             logger.info(f"Qdrant search (combined and sorted) returned {len(sorted_hits)} final results.")

#             # Build Chunk objects
#             found_chunks: List[Chunk] = []
#             for hit in sorted_hits:
#                 payload = hit["payload"] or {}
#                 metadata_fields = {k: v for k, v in payload.items() if k != "text"}
#                 if "file_path" not in metadata_fields:
#                     # Ensure file_path is present as it's a required field in ChunkMetadata
#                     metadata_fields["file_path"] = ""
#                 found_chunks.append(
#                     Chunk(
#                         id=hit["id"],
#                         text=payload.get("text", ""),
#                         metadata=ChunkMetadata(**metadata_fields),
#                         embedding=None
#                     )
#                 )
#             return found_chunks
#         except Exception as e:
#             logger.error(f"Error during Qdrant search in collection '{self.collection_name}': {e}", exc_info=True)
#             return []

#     def count_vectors(self) -> int:
#         try:
#             info = self.client.get_collection(collection_name=self.collection_name)
#             logger.info(f"Collection '{self.collection_name}' contains {info.points_count} vectors.")
#             return info.points_count
#         except Exception as e:
#             logger.error(f"Error getting collection info for '{self.collection_name}': {e}", exc_info=True)
#             return 0







from typing import List, Optional, Dict
import logging
from qdrant_client import QdrantClient, models
from qdrant_client.http.exceptions import UnexpectedResponse

from ..core.config import get_settings
from ..models.data_models import Chunk, ChunkMetadata

logger = logging.getLogger(__name__)

class QdrantService:
    def __init__(self):
        settings = get_settings()
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )

        # ✅ REQUIRED (THIS WAS MISSING)
        self.collection_name = "docusaurus_chunks"

        logger.info(
            f"Qdrant client initialized for remote instance at {settings.QDRANT_URL}, "
            f"collection='{self.collection_name}'"
        )

    def recreate_collection(self, vector_size: int):
        logger.info(
            f"Recreating collection '{self.collection_name}' with vector_size={vector_size}"
        )
        try:
            self.client.delete_collection(collection_name=self.collection_name)
        except UnexpectedResponse as e:
            if "not found" not in str(e):
                raise

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=models.Distance.COSINE,
            ),
        )

    def upsert_chunks(self, chunks: List[Chunk]):
        points = []
        for chunk in chunks:
            if not chunk.embedding or not chunk.text.strip():
                continue

            payload = (
                chunk.metadata.model_dump()
                if isinstance(chunk.metadata, ChunkMetadata)
                else chunk.metadata
            )
            payload["text"] = chunk.text

            points.append(
                models.PointStruct(
                    id=chunk.id,
                    vector=chunk.embedding,
                    payload=payload,
                )
            )

        if points:
            self.client.upsert(
                collection_name=self.collection_name,
                points=points,
                wait=True,
            )
            logger.info(f"Upserted {len(points)} chunks into Qdrant")

    def search_chunks(
        self,
        query_embedding: List[float],
        limit: int = 5,
        selected_text_embedding: Optional[List[float]] = None,
    ) -> List[Chunk]:

        logger.info(
            f"Searching Qdrant collection '{self.collection_name}' with limit={limit}"
        )

        def _process_response(response) -> Dict[str, Dict]:
            results = {}
            for hit in response:
                results[str(hit.id)] = {
                    "id": str(hit.id),
                    "score": hit.score,
                    "payload": hit.payload or {},
                }
            return results

        try:
            # ✅ CORRECT METHOD & PARAM
            response_query = self.client.query_points(
                collection_name=self.collection_name,
                vector=query_embedding,
                limit=limit,
                with_payload=True,
            )

            combined_results = _process_response(response_query)

            if selected_text_embedding:
                response_selected = self.client.query_points(
                    collection_name=self.collection_name,
                    vector=selected_text_embedding,
                    limit=limit,
                    with_payload=True,
                )
                selected_results = _process_response(response_selected)

                for pid, data in selected_results.items():
                    if (
                        pid not in combined_results
                        or data["score"] > combined_results[pid]["score"]
                    ):
                        combined_results[pid] = data

            sorted_hits = sorted(
                combined_results.values(),
                key=lambda x: x["score"],
                reverse=True,
            )[:limit]

            found_chunks: List[Chunk] = []
            for hit in sorted_hits:
                payload = hit["payload"]
                metadata_fields = {k: v for k, v in payload.items() if k != "text"}
                metadata_fields.setdefault("file_path", "")

                found_chunks.append(
                    Chunk(
                        id=hit["id"],
                        text=payload.get("text", ""),
                        metadata=ChunkMetadata(**metadata_fields),
                        embedding=None,
                    )
                )

            return found_chunks

        except Exception as e:
            logger.error(
                f"Qdrant search failed for collection '{self.collection_name}': {e}",
                exc_info=True,
            )
            return []

    def count_vectors(self) -> int:
        try:
            info = self.client.get_collection(
                collection_name=self.collection_name
            )
            return info.points_count
        except Exception as e:
            logger.error(e, exc_info=True)
            return 0
