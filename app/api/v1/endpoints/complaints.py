from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_complaints():
    return {"message": "List of complaints"}
