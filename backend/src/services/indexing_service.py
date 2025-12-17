# import os
# import hashlib
# from typing import List, Optional
# from datetime import datetime

# from backend.src.core.file_io import list_markdown_files, read_file_content
# from backend.src.models.data_models import DocusaurusBookContent, Chunk, ChunkMetadata
# from backend.src.services.chunking_service import ChunkingService
# from backend.src.services.embedding_service import EmbeddingService
# from backend.src.services.qdrant_service import QdrantService
# from backend.src.services.neon_service import NeonService

# import os
# import hashlib
# from typing import List, Optional
# from datetime import datetime

# from ..core.file_io import list_markdown_files, read_file_content
# from ..models.data_models import DocusaurusBookContent, Chunk, ChunkMetadata
# from .chunking_service import ChunkingService
# from .embedding_service import EmbeddingService
# from .qdrant_service import QdrantService
# from .neon_service import NeonService

# class IndexingService:
#     def __init__(
#         self,
#         qdrant_service: QdrantService,
#         neon_service: NeonService,
#         embedding_service: EmbeddingService,
#         chunking_service: ChunkingService,
#         book_content_dir: str = "book_source/docs",
#         specify_txt_path: str = "specify.txt" # Path to the specify.txt for change detection
#     ):
#         self.qdrant_service = qdrant_service
#         self.neon_service = neon_service
#         self.embedding_service = embedding_service
#         self.chunking_service = chunking_service
#         self.book_content_dir = book_content_dir
#         self.specify_txt_path = specify_txt_path

#     def _get_file_hash(self, file_path: str) -> Optional[str]:
#         """Generates an MD5 hash of a file's content."""
#         if not os.path.exists(file_path):
#             return None
#         with open(file_path, 'rb') as f:
#             return hashlib.md5(f.read()).hexdigest()

#     def _load_book_content(self) -> List[DocusaurusBookContent]:
#         """Reads all Markdown files from the Docusaurus book content directory."""
#         markdown_files = list_markdown_files(self.book_content_dir)
#         book_contents: List[DocusaurusBookContent] = []
#         for file_path in markdown_files:
#             content = read_file_content(file_path)
#             book_contents.append(DocusaurusBookContent(file_path=file_path, content=content))
#         return book_contents

#     def run_indexing_process(self, force_reindex: bool = False):
#         """
#         Runs the full indexing process for the Docusaurus book content.
#         If force_reindex is False, it performs change detection.
#         """
#         print("Starting indexing process...")
        
#         # --- Change Detection (T028 - Hybrid approach) ---
#         # For simplicity, we'll compare current file hashes/mtimes to what's in Neon (if implemented there)
#         # For now, a basic check. A full implementation would compare against stored hashes/mtimes for each file.
        
#         # This is a placeholder for actual change detection.
#         # A proper implementation would store metadata in Neon (e.g., hash of each file)
#         # and compare against that to determine if re-indexing is needed.
        
#         if not force_reindex:
#             # Check for changes in specify.txt (Q2: C - Hybrid)
#             current_specify_hash = self._get_file_hash(self.specify_txt_path)
#             # A full implementation would compare current_specify_hash with a stored hash
#             # For now, if not forced, we'll assume changes detected if no stored hash or if hashes differ.
#             # This part needs a database record to compare against.
#             print("Change detection is not fully implemented yet for automatic warnings.")
#             print("Please manually manage re-indexing or use --force.")
#             # For now, if not forced, we'll always proceed if no explicit state to compare against.

#         # --- Read and Chunk Book Content (T023 & T024) ---
#         book_contents = self._load_book_content()
#         all_chunks: List[Chunk] = []

#         # Assuming a default vector size for collection creation (e.g., from Gemini embedding model)
#         # In a real scenario, get this from the embedding service
#         embedding_vector_size = 768 # Example size, should be dynamic from model
#         self.qdrant_service.recreate_collection(vector_size=embedding_vector_size)
#         self.neon_service.create_tables()

#         for doc_content in book_contents:
#             # Extract basic metadata from file path, could be enhanced
#             file_name = os.path.basename(doc_content.file_path)
#             base_metadata = {"file_path": doc_content.file_path, "file_name": file_name}

#             chunks = self.chunking_service.chunk_text(
#                 text=doc_content.content,
#                 file_path=doc_content.file_path,
#                 metadata=base_metadata # This needs to be refined for heading/page/index
#             )
            
#             # --- Generate Embeddings and Store in Qdrant/Neon (T024, T025, T026) ---
#             for chunk in chunks:
#                 chunk.embedding = self.embedding_service.generate_embedding(chunk.text)
#                 chunk.metadata.page = 1 # Placeholder, need actual page parsing
#                 chunk.metadata.heading = "N/A" # Placeholder, need actual heading parsing
                
#                 # Store in Qdrant
#                 if chunk.embedding:
#                     self.qdrant_service.upsert_chunks([chunk])
                
#                 # Store in Neon
#                 self.neon_service.add_chunk_info(
#                     chunk_id=chunk.id,
#                     file_path=chunk.metadata.file_path,
#                     text=chunk.text,
#                     metadata=chunk.metadata.model_dump()
#                 )
#             all_chunks.extend(chunks)

#         print(f"Indexing process completed. Total chunks indexed: {len(all_chunks)}")




# import os
# import hashlib
# from typing import List, Optional
# from datetime import datetime

# from ..core.file_io import list_markdown_files, read_file_content
# from ..models.data_models import DocusaurusBookContent, Chunk, ChunkMetadata
# from .chunking_service import ChunkingService
# from .embedding_service import EmbeddingService
# from .qdrant_service import QdrantService
# from .neon_service import NeonService

# class IndexingService:
#     def __init__(
#         self,
#         qdrant_service: QdrantService,
#         neon_service: NeonService,
#         embedding_service: EmbeddingService,
#         chunking_service: ChunkingService,
#         book_content_dir: str = "book_source/docs",
#         specify_txt_path: str = "specify.txt"  # Path to the specify.txt for change detection
#     ):
#         self.qdrant_service = qdrant_service
#         self.neon_service = neon_service
#         self.embedding_service = embedding_service
#         self.chunking_service = chunking_service
#         self.book_content_dir = book_content_dir
#         self.specify_txt_path = specify_txt_path

#     def _get_file_hash(self, file_path: str) -> Optional[str]:
#         """Generates an MD5 hash of a file's content."""
#         if not os.path.exists(file_path):
#             return None
#         with open(file_path, 'rb') as f:
#             return hashlib.md5(f.read()).hexdigest()

#     def _load_book_content(self) -> List[DocusaurusBookContent]:
#         """Reads all Markdown files from the Docusaurus book content directory."""
#         markdown_files = list_markdown_files(self.book_content_dir)
#         book_contents: List[DocusaurusBookContent] = []

#         for idx, file_path in enumerate(markdown_files):
#             print(f"Processing file {idx+1}/{len(markdown_files)}: {file_path}")  # Progress print
#             content = read_file_content(file_path)
#             book_contents.append(DocusaurusBookContent(file_path=file_path, content=content))
#         return book_contents

#     def run_indexing_process(self, force_reindex: bool = False):
#         """
#         Runs the full indexing process for the Docusaurus book content.
#         If force_reindex is False, it performs change detection.
#         """
#         print("Starting indexing process...")

#         # --- Change Detection ---
#         if not force_reindex:
#             current_specify_hash = self._get_file_hash(self.specify_txt_path)
#             print("Change detection is not fully implemented yet for automatic warnings.")
#             print("Please manually manage re-indexing or use --force.")

#         # --- Read and Chunk Book Content ---
#         book_contents = self._load_book_content()
#         all_chunks: List[Chunk] = []

#         embedding_vector_size = 768  # Example size
#         self.qdrant_service.recreate_collection(vector_size=embedding_vector_size)
#         self.neon_service.create_tables()

#         for doc_idx, doc_content in enumerate(book_contents):
#             file_name = os.path.basename(doc_content.file_path)
#             base_metadata = {"file_path": doc_content.file_path, "file_name": file_name}

#             chunks = self.chunking_service.chunk_text(
#                 text=doc_content.content,
#                 file_path=doc_content.file_path,
#                 metadata=base_metadata
#             )

#             for chunk_idx, chunk in enumerate(chunks):
#                 print(f"Processing chunk {chunk_idx+1}/{len(chunks)} for file {file_name}")  # Chunk progress
#                 chunk.embedding = self.embedding_service.generate_embedding(chunk.text)
#                 chunk.metadata.page = 1  # Placeholder
#                 chunk.metadata.heading = "N/A"  # Placeholder

#                 # Store in Qdrant
#                 if chunk.embedding:
#                     self.qdrant_service.upsert_chunks([chunk])

#                 # Store in Neon
#                 self.neon_service.add_chunk_info(
#                     chunk_id=chunk.id,
#                     file_path=chunk.metadata.file_path,
#                     text=chunk.text,
#                     metadata=chunk.metadata.model_dump()
#                 )

#             all_chunks.extend(chunks)

#         print(f"Indexing process completed. Total chunks indexed: {len(all_chunks)}")


import os
import hashlib
from typing import List, Optional
from datetime import datetime
import asyncio

from ..core.file_io import list_markdown_files, read_file_content
from ..models.data_models import DocusaurusBookContent, Chunk
from .chunking_service import ChunkingService
from .embedding_service import EmbeddingService
from .qdrant_service import QdrantService
from .neon_service import NeonService

class IndexingService:
    def __init__(
        self,
        qdrant_service: QdrantService,
        neon_service: NeonService,
        embedding_service: EmbeddingService,
        chunking_service: ChunkingService,
        book_content_dir: str = "book_source/docs",
        specify_txt_path: str = "specify.txt"
    ):
        self.qdrant_service = qdrant_service
        self.neon_service = neon_service
        self.embedding_service = embedding_service
        self.chunking_service = chunking_service
        self.book_content_dir = book_content_dir
        self.specify_txt_path = specify_txt_path

    def _get_file_hash(self, file_path: str) -> Optional[str]:
        """Generates an MD5 hash of a file's content."""
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def _load_book_content(self) -> List[DocusaurusBookContent]:
        """Reads all Markdown files from the Docusaurus book content directory."""
        markdown_files = list_markdown_files(self.book_content_dir)
        book_contents: List[DocusaurusBookContent] = []

        for idx, file_path in enumerate(markdown_files):
            print(f"Processing file {idx+1}/{len(markdown_files)}: {file_path}")
            content = read_file_content(file_path)
            book_contents.append(DocusaurusBookContent(file_path=file_path, content=content))
        return book_contents

    async def run_indexing_process(self, force_reindex: bool = False):
        """
        Async: Runs the full indexing process for the Docusaurus book content.
        """
        print("Starting indexing process...")

        # --- Change Detection ---
        if not force_reindex:
            current_specify_hash = self._get_file_hash(self.specify_txt_path)
            print("Change detection is not fully implemented yet for automatic warnings.")
            print("Please manually manage re-indexing or use --force.")

        # --- Read and Chunk Book Content ---
        book_contents = self._load_book_content()
        all_chunks: List[Chunk] = []

        embedding_vector_size = 1536
        self.qdrant_service.recreate_collection(vector_size=embedding_vector_size)
        self.neon_service.create_tables()

        for doc_idx, doc_content in enumerate(book_contents):
            file_name = os.path.basename(doc_content.file_path)
            base_metadata = {"file_path": doc_content.file_path, "file_name": file_name}

            chunks = self.chunking_service.chunk_text(
                text=doc_content.content,
                file_path=doc_content.file_path,
                metadata=base_metadata
            )

            for chunk_idx, chunk in enumerate(chunks):
                print(f"Processing chunk {chunk_idx+1}/{len(chunks)} for file {file_name}")
                
                # 🔹 Async embedding generation
                chunk.embedding = await self.embedding_service.generate_embedding(chunk.text)
                
                chunk.metadata.page = 1
                chunk.metadata.heading = "N/A"

                # Store in Qdrant
                if chunk.embedding:
                    self.qdrant_service.upsert_chunks([chunk])

                # Store in Neon
                self.neon_service.add_chunk_info(
                    chunk_id=chunk.id,
                    file_path=chunk.metadata.file_path,
                    text=chunk.text,
                    metadata=chunk.metadata.model_dump()
                )

            all_chunks.extend(chunks)

        print(f"Indexing process completed. Total chunks indexed: {len(all_chunks)}")
