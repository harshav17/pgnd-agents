from pathlib import Path
import chromadb
from chromadb.config import Settings
from .paths import get_data_dir
import chromadb.utils.embedding_functions as embedding_functions

class ChromaDBHandler:
    """Handles ChromaDB initialization and operations."""
    
    @staticmethod
    def get_db_path() -> Path:
        """Get the ChromaDB storage path within data directory."""
        db_path = get_data_dir() / "chroma_db"
        db_path.mkdir(exist_ok=True)
        return db_path
    
    @staticmethod
    def get_embedding_function(key: str):
        openai_ef = embedding_functions.OpenAIEmbeddingFunction(
            api_key=key,
            model_name="text-embedding-3-small"
        )
        return openai_ef

    @classmethod
    def get_client(cls, persist: bool = True) -> chromadb.Client:
        """
        Initialize and return a ChromaDB client.
        
        Args:
            persist (bool): If True, uses persistent storage. If False, uses in-memory.
        
        Returns:
            chromadb.Client: Initialized ChromaDB client
        """
        # TODO add an embedding function to the clients

        if persist:
            db_path = cls.get_db_path()
            client = chromadb.PersistentClient(
                path=str(db_path),
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )
        else:
            client = chromadb.Client(Settings(
                anonymized_telemetry=False,
                allow_reset=True
            ))
            
        return client