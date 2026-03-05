from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Type Safe API"
    debug: bool = False
    database_url : str = "postgresql://postgres:Raki@123@localhost:5432/type_safe_api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid"
    )
 # model_config = SettingsConfigDict(
 #        env_file=".env",
 #        env_file_encoding="utf-8",
 #        extra="forbid"
 #    )


settings = Settings()