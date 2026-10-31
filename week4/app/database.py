
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration
DATABASE_URL = "sqlite:///hospital.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# Base class for all database models
Base = declarative_base()

# Create session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
