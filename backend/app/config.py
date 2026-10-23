from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Smart SCM Agentic AI"
    database_url: str = "sqlite:///./smart_scm.db"
    ai_provider: str = "demo"
    openai_api_key: str = ""
    openai_model: str = ""
    frontend_origin: str = "http://localhost:5173"
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

settings = Settings()
