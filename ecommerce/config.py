from pydantic import BaseSettings


class Settings(BaseSettings):
    database_engine:str
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    
    class Config:
        env_file=".env"

settings = Settings()