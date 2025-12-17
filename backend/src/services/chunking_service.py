import uuid
from typing import List, Dict
from backend.src.models.data_models import Chunk, ChunkMetadata

class ChunkingService:
    def __init__(self, chunk_size: int = 300, chunk_overlap: int = 50):
        # Default chunk size and overlap, can be made configurable
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str, file_path: str, metadata: Dict[str, str] = None) -> List[Chunk]:
        """Breaks a given text into smaller chunks with overlap."""
        chunks: List[Chunk] = []
        words = text.split()
        
        # Ensure chunk_size is within 150-400 words
        current_chunk_size = max(150, min(self.chunk_size, 400))
        
        i = 0
        while i < len(words):
            chunk_words = words[i : i + current_chunk_size]
            chunk_text = " ".join(chunk_words)

            # Generate a unique ID for the chunk
            chunk_id = str(uuid.uuid4())

            # Prepare metadata for the chunk
            chunk_metadata = ChunkMetadata(
                heading=metadata.get("heading"),
                page=metadata.get("page"),
                index=i, # Simple word index, could be more sophisticated
                file_path=file_path
            )

            chunks.append(
                Chunk(
                    id=chunk_id,
                    text=chunk_text,
                    metadata=chunk_metadata,
                    embedding=None # Embedding will be added later
                )
            )
            
            i += (current_chunk_size - self.chunk_overlap)
            if i < 0: # Ensure index doesn't go negative if overlap is too large
                i = 0
        
        # Handle cases where the last chunk might be too small
        if chunks and len(words) > 0:
            last_chunk = chunks[-1]
            if len(last_chunk.text.split()) < 50 and len(chunks) > 1: # Arbitrary small chunk threshold
                # Merge small last chunk with the previous one
                chunks[-2].text += " " + last_chunk.text
                chunks.pop()

        return chunks
