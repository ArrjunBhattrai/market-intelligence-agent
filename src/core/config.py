from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Market Intelligence Agent"

    class Config:
        env_file = ".env"

settings = Settings()
