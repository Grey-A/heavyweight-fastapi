import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Security
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    HASHING_ALGORITHM: str = os.environ.get("HASHING_ALGORITHM")

    # DB Settings
    POSTGRES_USER: str = os.environ.get("PGUSER")
    POSTGRES_PASSWORD: str = os.environ.get("PGPASSWORD")
    POSTGRES_SERVER: str = os.environ.get("PGHOST")
    POSTGRES_PORT: int = os.environ.get("PGPORT")
    POSTGRES_DB: str = os.environ.get("PGDATABASE")

    class Config:
        env_file = ".env"

    @property
    def POSTGRES_URL(self):
        url = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return url


settings = Settings()
