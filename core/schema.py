from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Text
from sqlalchemy.sql import func
from core.db import Base

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())

class Session(Base):
    __tablename__ = "sessions"
    id = Column(String, primary_key=True)
    student_id = Column(String, ForeignKey("students.id", ondelete="CASCADE"))
    date = Column(DateTime)

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(String, primary_key=True)
    session_id = Column(String, ForeignKey("sessions.id", ondelete="CASCADE"))
    question = Column(Text)
    answer = Column(Text)
    cognitive_tag = Column(Text)
    psychologist_notes = Column(Text)
    confidence = Column(Integer)

Base.metadata.create_all(engine)
print("✅ Tables created in PostgreSQL.")
