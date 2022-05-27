from functools import lru_cache

from pydantic import BaseSettings

class Settings(BaseSettings):
    CACHE_TYPE = ""
    CACHE_REDIS_HOST = ""
    CACHE_REDIS_PORT = ""
    CACHE_REDIS_DB = ""
    CACHE_REDIS_URL = ""
    CACHE_DEFAULT_TIMEOUT = ""

@lru_cache()
def get_settings():
    return Settings()
