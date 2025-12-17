from sqlalchemy import create_engine, Column, String, Text, Float, DateTime, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ..core.config import get_settings
from ..models.data_models import ChunkMetadata # Import if needed for JSON field type

# Define the base for declarative models
Base = declarative_base()

class BookChunk(Base):
    __tablename__ = 'book_chunks'

    id = Column(String, primary_key=True, index=True) # Corresponds to Chunk.id
    file_path = Column(String, nullable=False, index=True)
    text = Column(Text, nullable=False) # Store the chunk text
    metadata_json = Column(JSON, nullable=False) # Store ChunkMetadata as JSON
    indexing_timestamp = Column(DateTime, default=datetime.utcnow)
    # Add other fields as needed, e.g., page, heading, etc. directly or from metadata_json

    def __repr__(self):
        return f"<BookChunk(id='{self.id}', file_path='{self.file_path}')>"

class NeonService:
    def __init__(self):
        settings = get_settings()
        self.engine = create_engine(settings.NEON_POSTGRES_CONN_STR)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        """Creates all defined tables in the database."""
        Base.metadata.create_all(bind=self.engine)
        print("Database tables created/verified.")

    def add_chunk_info(self, chunk_id: str, file_path: str, text: str, metadata: Dict[str, Any]):
        """Adds or updates chunk information in the database."""
        db = self.SessionLocal()
        try:
            db_chunk = db.query(BookChunk).filter(BookChunk.id == chunk_id).first()
            if db_chunk:
                db_chunk.file_path = file_path
                db_chunk.text = text
                db_chunk.metadata_json = metadata
                db_chunk.indexing_timestamp = datetime.utcnow()
                print(f"Updated chunk info for ID: {chunk_id}")
            else:
                db_chunk = BookChunk(
                    id=chunk_id,
                    file_path=file_path,
                    text=text,
                    metadata_json=metadata,
                    indexing_timestamp=datetime.utcnow()
                )
                db.add(db_chunk)
                print(f"Added chunk info for ID: {chunk_id}")
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    def get_chunk_info(self, chunk_id: str):
        """Retrieves chunk information by ID."""
        db = self.SessionLocal()
        try:
            return db.query(BookChunk).filter(BookChunk.id == chunk_id).first()
        finally:
            db.close()
