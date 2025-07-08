# dbconfig.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# ------------------------------
# ✅ DATABASE CONFIGURATION
# ------------------------------

# Example for MySQL:
# DATABASE_URL = "mysql+pymysql://username:password@localhost/technobot_db"

# Example for PostgreSQL:
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost/technobot_db"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///technobot.db")  # fallback to SQLite

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL logs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
