from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Type Safe API"
    debug: bool = False


settings = Settings()