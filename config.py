from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str = Field(default="sqlite:///aitutor.db")

    class Config:
        env_file = ".env"          # optional
        env_file_encoding = "utf-8"

settings = Settings()
