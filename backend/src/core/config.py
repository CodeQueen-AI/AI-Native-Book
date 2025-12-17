# from pydantic_settings import BaseSettings, SettingsConfigDict
# from functools import lru_cache

# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(env_file=".env", extra="ignore")

#     QDRANT_API_KEY: str
#     QDRANT_URL: str
#     NEON_POSTGRES_CONN_STR: str


#     # Add any other configurations here

# @lru_cache
# def get_settings():
#     return Settings()
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"),
        extra="ignore"
    )

    QDRANT_API_KEY: str
    QDRANT_URL: str
    NEON_POSTGRES_CONN_STR: str
    OPENROUTER_API_KEY: str
    OPENROUTER_EMBEDDING_MODEL_NAME: str

@lru_cache
def get_settings():
    return Settings()
