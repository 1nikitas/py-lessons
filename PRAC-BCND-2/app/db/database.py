from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote_plus

# URL encode the password if it contains special characters
password = quote_plus("%0.}7Y1h-;R*@O")
SQLALCHEMY_DATABASE_URL = f"postgresql://gen_user:{password}@147.45.237.134:5432/default_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)
