from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str
    ALLOWED_ORIGINS: str = ""
    # GOOGLE_GEMINI_API_KEY: str
    
    @field_validator("ALLOWED_ORIGINS")
    def validate_allowed_origins(cls, v: str) -> List[str]:
        return v.split("," ) if v else []
    
    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()
    