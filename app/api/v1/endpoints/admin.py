from fastapi import APIRouter, HTTPException
from app.core.database import complaints_collection, requests_collection
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter()


class AdminUpdateRequest(BaseModel):
    request_id: str
    status: str  # "approved" or "rejected"


@router.get("/complaints")
async def get_all_complaints():
    complaints = await complaints_collection.find().to_list(None)
    return complaints


@router.get("/requests")
async def get_all_requests():
    requests = await requests_collection.find().to_list(None)
    return requests


@router.put("/update-status")
async def update_status(data: AdminUpdateRequest):
    if data.status not in ["approved", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    collection = complaints_collection if "complaint" in data.request_id else requests_collection
    update_result = await collection.update_one({"_id": ObjectId(data.request_id)}, {"$set": {"status": data.status}})

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Request not found")

    return {"message": f"Request {data.request_id} updated to {data.status}"}
