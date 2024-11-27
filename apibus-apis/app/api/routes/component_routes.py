from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from app.utils.access_control import get_current_user_by_jwt
from app.utils.access_control import RoleChecker
from starlette import status
from app.utils import constants

router = APIRouter()


# PHPIPAM Integration Endpoints
@router.get("/phpipam", response_model=List[str])
async def get_phpipam_components(current_user=Depends(get_current_user_by_jwt)):
    return list(constants.phpipam_components.keys())


@router.get("/phpipam/{component}", response_model=List[str])
async def get_phpipam_component_params(component: str, current_user=Depends(get_current_user_by_jwt)):
    if component not in constants.phpipam_components:
        raise HTTPException(status_code=404, detail="Component not found")
    return list(constants.phpipam_components[component])


# Corero Integration Endpoints
@router.get("/corero", response_model=List[str])
async def get_corero_components(current_user=Depends(get_current_user_by_jwt)):
    return list(constants.corero_components.keys())


@router.get("/corero/{component}", response_model=List[str])
async def get_corero_component_params(component: str, current_user=Depends(get_current_user_by_jwt)):
    if component not in constants.corero_components:
        raise HTTPException(status_code=404, detail="Component not found")
    return list(constants.corero_components[component])
