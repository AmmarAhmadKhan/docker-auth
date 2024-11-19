from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy import Column, String, Integer, JSON, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import jwt
import os
from passlib.context import CryptContext

# Configuration
DATABASE_URL = "sqlite:///./automaton.db"
SECRET_KEY = "omitted for github repo"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class Automaton(Base):
    __tablename__ = 'automaton'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    node_details = Column(JSON)
    connection_details = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String)


Base.metadata.create_all(bind=engine)


class AutomatonCreate(BaseModel):
    name: str
    description: Optional[str] = None
    node_details: dict
    connection_details: dict

class AutomatonResponse(AutomatonCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    created_by: str


app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


api_users_db = {

}

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(api_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(api_users_db, username)
    if user is None:
        raise credentials_exception
    return user


@app.post("/automatons/", response_model=AutomatonResponse)
async def create_automaton(automaton: AutomatonCreate, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    db_automaton = Automaton(**automaton.dict(), created_by=current_user.username)
    db.add(db_automaton)
    db.commit()
    db.refresh(db_automaton)
    return db_automaton

@app.get("/automatons/", response_model=List[AutomatonResponse])
async def get_automatons(skip: int = 0, limit: int = 10, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    automatons = db.query(Automaton).offset(skip).limit(limit).all()
    return automatons

@app.get("/automatons/{automaton_id}", response_model=AutomatonResponse)
async def get_automaton(automaton_id: int, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
    if automaton is None:
        raise HTTPException(status_code=404, detail="Automaton not found")
    return automaton

@app.put("/automatons/{automaton_id}", response_model=AutomatonResponse)
async def update_automaton(automaton_id: int, automaton: AutomatonCreate, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    db_automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
    if db_automaton is None:
        raise HTTPException(status_code=404, detail="Automaton not found")
    for key, value in automaton.dict().items():
        setattr(db_automaton, key, value)
    db_automaton.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_automaton)
    return db_automaton

@app.delete("/automatons/{automaton_id}")
async def delete_automaton(automaton_id: int, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
    if automaton is None:
        raise HTTPException(status_code=404, detail="Automaton not found")
    db.delete(automaton)
    db.commit()
    return {"detail": "Automaton deleted"}