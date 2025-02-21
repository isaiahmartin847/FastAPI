from fastapi import FastAPI
from app.api.v1.endpoints.api import router as api_router

app = FastAPI()

# Include the API router
app.include_router(api_router, prefix="/api/v1")