# app/core/config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    model_version: str = "v1"
    # add other settings like DB_URL, LOG_LEVEL loaded from env
    class Config:
        env_file = ".env"  # for local dev only

settings = Settings()
