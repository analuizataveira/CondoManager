from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/gestaopredial")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
