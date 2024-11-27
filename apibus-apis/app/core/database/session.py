import os
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import ProgrammingError
from .models import Base, User
from passlib.context import CryptContext

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your PostgreSQL connection string
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'apibus-postgres')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'apibus-db')
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# Create an engine
engine = create_engine(DATABASE_URL)

try:
    if not database_exists(engine.url):
        logger.info("Database not found")
        create_database(engine.url)
        logger.info("Database created")
    else:
        logger.info(f"Database {POSTGRES_DB} Already Exists")
    Base.metadata.create_all(engine)
except ProgrammingError as e:
    logger.error(f"An error occurred while creating tables: {e}")

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_default_user():
    session = SessionLocal()
    try:
        admin_user = session.query(User).filter_by(username='apiuser').first()
        if not admin_user:
            pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
            hashed_password = pwd_context.hash("1line@atime")
            admin_user = User(
                username="apiuser",
                full_name="API User",
                email="api@user.com",
                password=hashed_password,
                level=0,
                active=1
            )
            session.add(admin_user)
            session.commit()
            logger.info("Default apiuser user created")
        else:
            logger.info("apiuser user already exists")
    except Exception as e:
        session.rollback()
        logger.error(f"An error occurred while creating the default apiuser user: {e}")
    finally:
        session.close()


# Call the function to create the default user
create_default_user()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
