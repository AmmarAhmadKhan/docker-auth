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

    automatons = relationship("Automaton", back_populates="creator")

    __table_args__ = (
        UniqueConstraint('username', name='username'),
    )


class Automaton(Base):
    __tablename__ = 'automaton'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(String, index=True)
    node_details = Column(JSON, nullable=True)
    connection_details = Column(JSON, nullable=True)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)  # Foreign key to User
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    creator = relationship("User", back_populates="automatons")


class APIConfig(Base):
    __tablename__ = 'api_config'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    url = Column(String, index=True, unique=True)
    ip = Column(String)
    port = Column(String)
    api_key = Column(String)
    api_doc_url = Column(String)
    status = Column(String)

    __table_args__ = (
        UniqueConstraint('ip', 'port', name='unique_ip_port'),
    )


class Normalizer(Base):
    __tablename__ = 'normalizer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    description = Column(String, index=True)
    node_details = Column(JSON, nullable=True)
