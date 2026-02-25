from pydantic import BaseSettings

#Base class type is unknown, obscuring type of derived class
class Settings(BaseSettings):
    app_name: str = "Type Safe API"
    debug: bool = False


settings = Settings()