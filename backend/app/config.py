from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "CVGenerator"
    cors_allow_origins: list = ["*"]

    debug: bool = False

    openai_api_key: str
    openai_model: str


settings = Settings()
