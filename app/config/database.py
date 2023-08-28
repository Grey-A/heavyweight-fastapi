from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config.settings import settings

engine = create_engine(
    url=settings.POSTGRES_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBBase = declarative_base()
