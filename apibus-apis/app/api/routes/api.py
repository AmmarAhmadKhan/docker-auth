from fastapi import APIRouter

from app.api.routes.auth_routes import router as auth_router
from app.api.routes.user_routes import router as user_router
from app.api.routes.automaton_routes import router as automaton_router
from app.api.routes.component_routes import router as component_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/api/auth", tags=["AUTH"])
api_router.include_router(user_router, prefix="/api/user", tags=["USER"])
api_router.include_router(automaton_router, prefix="/api/automaton", tags=["AUTOMATON"])
api_router.include_router(component_router, prefix="/api/component", tags=["COMPONENT"])
