# app/config.py
from functools import lru_cache # For caching the settings instance
from pydantic_settings import BaseSettings # For defining the settings model

# Application configuration using Pydantic's BaseSettings for environment variable management and validation.
class Settings(BaseSettings):
    # Database connection default settings fallback if .env file is not present/incomplete
    database_url: str = "postgresql://hoi4:hoi4pass@localhost:5432/hoi4"
    app_title: str = "HOI4 API"
    app_version: str = "1.0.0"

    # Pagination default settings
    default_page_size: int = 50
    max_page_size: int = 500

    # Game date parameters: prevents SQL injection by restricting to known valid dates
    default_date: str = "1936-01-01" # Default date for queries if none specified
    allowed_dates: list[str] = ["1936-01-01", "1939-08-14"] # Allowed dates for queries, reject anything else.
 
    # Configuration settings for loading from .env file.
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}
# End of Settings class.

# Optimisation: Cache the settings instance to avoid reloading on every access, settings are resource-intensive to create.
@lru_cache() # least recently used cache decorator to store the first settings instance.
def get_settings() -> Settings: # Get a settings instance
    return Settings() # Return the new instance from the cached Settings instance.
# End of get_settings function.
