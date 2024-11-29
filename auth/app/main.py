from fastapi import FastAPI, HTTPException, Depends, status
from typing import List, Dict, Optional
from app.api.routes.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
import inspect

app = FastAPI()

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)


def custom_openapi():
    """Implementation for Custom Swagger UI: This code scans all endpoint functions that have a JWT dependency in
    their body, including the function definition line. It then adds an Authorization header to all those endpoints,
    simplifying testing by enabling the use of the Authorize Button, akin to how we use it for oauth2_scheme =
    OAuth2PasswordBearer."""

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="FastAPI Auth Service - CUSTOM SWAGGER UI",
        version="1.0.0",
        description="FastAPI Auth Service APIs with an Authorize Button",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
        }
    }

    # Get all routes which are instances of APIRoute
    api_router = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_router:
        path = getattr(route, "path")
        endpoint = getattr(route, "endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]
        # Get the signature of the endpoint function
        endpoint_signature = inspect.signature(endpoint)

        # Check if the endpoint function has specific parameter names
        if "current_user" in endpoint_signature.parameters or \
                "credentials" in endpoint_signature.parameters:

            for method in methods:
                openapi_schema["paths"][path][method]["security"] = [{"Bearer Auth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
