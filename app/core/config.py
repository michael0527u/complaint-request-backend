import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URI: str = os.getenv("MONGODB_URI")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1/chat/completions"

settings = Settings()
