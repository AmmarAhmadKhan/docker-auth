from sqlalchemy import Column, JSON, Integer, String, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    full_name = Column(String(80))
    password = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    email = Column(String)
    active = Column(Integer, default=1, nullable=False)
    mobile = Column(String, default=None)
    password_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('username', name='username'),
    )
