from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from app.utils.access_control import get_current_user_by_jwt
from app.utils.access_control import RoleChecker
from starlette import status
from app.core.database.models import Automaton
from app.core.database.session import SessionLocal, Session, get_db
from app.api.models import AutomatonResponse, AutomatonCreate
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("", response_model=AutomatonResponse)
async def create_automaton(automaton: AutomatonCreate,
                           db: Session = Depends(get_db),
                           current_user=Depends(get_current_user_by_jwt)):
    try:
        db_automaton = Automaton(**automaton.dict(), created_by=current_user.id)
        db.add(db_automaton)
        db.commit()
        db.refresh(db_automaton)
        return db_automaton
    except IntegrityError as e:
        db.rollback()
        if 'unique constraint' in str(e).lower():
            raise HTTPException(status_code=400, detail="Automaton with this name already exists.")
        else:
            raise HTTPException(status_code=500, detail="An error occurred while creating the automaton.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=List[AutomatonResponse])
async def get_automatons(skip: int = 0, limit: int = 10,
                         db: Session = Depends(get_db),
                         current_user=Depends(get_current_user_by_jwt)):
    automatons = db.query(Automaton).options(joinedload(Automaton.creator)).offset(skip).limit(limit).all()
    return automatons


@router.get("/{automaton_id}", response_model=AutomatonResponse)
async def get_automaton(automaton_id: int,
                        db: Session = Depends(get_db),
                        current_user=Depends(get_current_user_by_jwt)):
    automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
    if automaton is None:
        raise HTTPException(status_code=404, detail="Automaton not found")
    return automaton


@router.put("/{automaton_id}", response_model=AutomatonResponse)
async def update_automaton(automaton_id: int, automaton: AutomatonCreate,
                           db: Session = Depends(get_db),
                           current_user=Depends(get_current_user_by_jwt)):
    try:
        db_automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
        if db_automaton is None:
            raise HTTPException(status_code=404, detail="Automaton not found")
        for key, value in automaton.dict().items():
            setattr(db_automaton, key, value)
        db_automaton.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_automaton)
        return db_automaton
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{automaton_id}")
async def delete_automaton(automaton_id: int,
                           db: Session = Depends(get_db),
                           current_user=Depends(get_current_user_by_jwt)):
    try:
        automaton = db.query(Automaton).filter(Automaton.id == automaton_id).first()
        if automaton is None:
            raise HTTPException(status_code=404, detail="Automaton not found")
        db.delete(automaton)
        db.commit()
        return {"detail": "Automaton deleted"}
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
