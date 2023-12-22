from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Config:
    database_url: str

def load_config_from_env():
    database_name = os.getenv('DB_NAME', 'library')
    user = os.getenv('DB_USER', 'postgres')
    password = os.getenv('DB_PASSWORD', '1234')
    host = os.getenv('DB_HOST', 'localhost')

    database_url = f"postgresql://{user}:{password}@{host}/{database_name}"

    return Config(database_url)


config = load_config_from_env()

engine = create_engine(config.database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()