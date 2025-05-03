# core/db.py

import os
import sqlalchemy
from google.cloud.sql.connector import Connector
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialize the Cloud SQL connector
connector = Connector()

def getconn():
    return connector.connect(
        "trans-mind-458703-e1:us-central1:cognitive",  # GCP instance
        "pg8000",
        user="postgres",
        password="gcptara",
        db="postgres",
    )

# SQLAlchemy engine using the custom connection function
engine = sqlalchemy.create_engine("postgresql+pg8000://", creator=getconn)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
