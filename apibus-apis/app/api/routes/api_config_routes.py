from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from app.utils.access_control import get_current_user_by_jwt
from app.utils.access_control import RoleChecker
from starlette import status
from app.core.database.models import APIConfig
from app.core.database.session import SessionLocal, Session, get_db
from app.api.models import APIConfigResponse, APIConfigCreate
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("", response_model=APIConfigResponse)
async def create_api_config(apiConfig: APIConfigCreate,
                            db: Session = Depends(get_db),
                            current_user=Depends(get_current_user_by_jwt)):
    try:
        db_apiConfig = APIConfig(**apiConfig.dict())
        db.add(db_apiConfig)
        db.commit()
        db.refresh(db_apiConfig)
        return db_apiConfig
    except IntegrityError as e:
        db.rollback()
        if 'unique constraint' in str(e).lower():
            raise HTTPException(status_code=400, detail="Duplicate APIConfig already exists.")
        else:
            raise HTTPException(status_code=500, detail="An error occurred while creating the API Config.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=List[APIConfigResponse])
async def get_apiConfigs(skip: int = 0, limit: int = 10,
                         db: Session = Depends(get_db),
                         current_user=Depends(get_current_user_by_jwt)):
    apiConfigs = db.query(APIConfig).offset(skip).limit(limit).all()
    return apiConfigs


@router.get("/{id}", response_model=APIConfigResponse)
async def get_apiConfig(id: int,
                        db: Session = Depends(get_db),
                        current_user=Depends(get_current_user_by_jwt)):
    apiConfig = db.query(APIConfig).filter(APIConfig.id == id).first()
    if apiConfig is None:
        raise HTTPException(status_code=404, detail="APIConfig not found")
    return apiConfig


@router.put("/{id}", response_model=APIConfigResponse)
async def update_apiConfig(id: int, apiConfig: APIConfigCreate,
                           db: Session = Depends(get_db),
                           current_user=Depends(get_current_user_by_jwt)):
    try:
        db_apiConfig = db.query(APIConfig).filter(APIConfig.id == id).first()
        if db_apiConfig is None:
            raise HTTPException(status_code=404, detail="APIConfig not found")
        for key, value in apiConfig.dict().items():
            setattr(db_apiConfig, key, value)
        db.commit()
        db.refresh(db_apiConfig)
        return db_apiConfig
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{apiConfig_id}")
async def delete_apiConfig(apiConfig_id: int,
                           db: Session = Depends(get_db),
                           current_user=Depends(get_current_user_by_jwt)):
    try:
        apiConfig = db.query(APIConfig).filter(APIConfig.id == apiConfig_id).first()
        if apiConfig is None:
            raise HTTPException(status_code=404, detail="APIConfig not found")
        db.delete(apiConfig)
        db.commit()
        return {"detail": "APIConfig deleted"}
    except HTTPException as e:
        db.rollback()
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
