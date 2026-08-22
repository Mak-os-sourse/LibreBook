import os
from dotenv import load_dotenv

if not load_dotenv("settings.env"):
    raise ValueError("Not found settings.env")

class Settings:
    jwt_key: str = os.getenv("JWT_KEY")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    jwt_refresh_exp: int = int(os.getenv("JWT_REFRESH_EXP", 3600))
    jwt_access_exp: int = int(os.getenv("JWT_ACCESS_EXP", 15 * 60))
    
settings = Settings()