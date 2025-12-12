from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 服务端配置
    API_PREFIX: str = "/v1"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # 代理鉴权
    PROXY_API_KEYS: List[str] = ["sk-123456"] 
    
    # Anuneko 配置 (必需)
    ANUNEKO_TOKEN: str = "x-token" 
    ANUNEKO_COOKIE: str = ""
    
    # API 接口地址
    BASE_URL: str = "https://anuneko.ai/api/v1"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
