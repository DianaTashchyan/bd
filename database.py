from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://postgres:1234@localhost:5432/library"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base(metadata=MetaData())


Base.metadata.create_all(engine)
