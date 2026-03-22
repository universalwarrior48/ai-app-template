"""
Configuration module for the AI application.
"""

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Application
    app_name: str = "AI Application"
    debug: bool = False

    # Models
    model_name: str = "default-model"
    model_path: Optional[str] = None

    # Services
    vector_db_url: str = "http://localhost:8000"
    cache_ttl: int = 3600  # 1 hour

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # UI
    ui_port: int = 7860

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
