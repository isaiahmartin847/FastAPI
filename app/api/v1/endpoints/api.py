from fastapi import APIRouter

router = APIRouter()

# Define your API endpoints here
@router.get("/")
async def read_root():
    return {"message": "Hello, World!"} 