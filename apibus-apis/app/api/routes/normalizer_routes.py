from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from app.utils.access_control import get_current_user_by_jwt
from app.utils.access_control import RoleChecker
from starlette import status
from app.core.database.models import Normalizer
from app.core.database.session import SessionLocal, Session, get_db
from app.api.models import NormalizerResponse, NormalizerCreate
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("", response_model=NormalizerResponse)
async def create_normalizer(normalizer: NormalizerCreate,
                            db: Session = Depends(get_db),
                            current_user=Depends(get_current_user_by_jwt)):
    try:
        db_normalizer = Normalizer(**normalizer.dict())
        db.add(db_normalizer)
        db.commit()
        db.refresh(db_normalizer)
        return db_normalizer
    except IntegrityError as e:
        db.rollback()
        if 'unique constraint' in str(e).lower():
            raise HTTPException(status_code=400, detail="Normalizer with this name already exists.")
        else:
            raise HTTPException(status_code=500, detail="An error occurred while creating the normalizer.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=List[NormalizerResponse])
async def get_normalizers(skip: int = 0, limit: int = 10,
                          db: Session = Depends(get_db),
                          current_user=Depends(get_current_user_by_jwt)):
    normalizers = db.query(Normalizer).offset(skip).limit(limit).all()
    return normalizers


@router.get("/{id}", response_model=NormalizerResponse)
async def get_normalizer(id: int,
                         db: Session = Depends(get_db),
                         current_user=Depends(get_current_user_by_jwt)):
    normalizer = db.query(Normalizer).filter(Normalizer.id == id).first()
    if normalizer is None:
        raise HTTPException(status_code=404, detail="Normalizer not found")
    return normalizer


@router.put("/{id}", response_model=NormalizerResponse)
async def update_normalizer(id: int, normalizer: NormalizerCreate,
                            db: Session = Depends(get_db),
                            current_user=Depends(get_current_user_by_jwt)):
    try:
        db_normalizer = db.query(Normalizer).filter(Normalizer.id == id).first()
        if db_normalizer is None:
            raise HTTPException(status_code=404, detail="Normalizer not found")
        for key, value in normalizer.dict().items():
            setattr(db_normalizer, key, value)
        db_normalizer.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_normalizer)
        return db_normalizer
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{id}")
async def delete_normalizer(id: int,
                            db: Session = Depends(get_db),
                            current_user=Depends(get_current_user_by_jwt)):
    try:
        normalizer = db.query(Normalizer).filter(Normalizer.id == id).first()
        if normalizer is None:
            raise HTTPException(status_code=404, detail="Normalizer not found")
        db.delete(normalizer)
        db.commit()
        return {"detail": "Normalizer deleted"}
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
