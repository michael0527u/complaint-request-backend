from fastapi import APIRouter, HTTPException
from app.services.chatbot_service import generate_letter
from app.core.database import complaints_collection, requests_collection
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

# ✅ Define request model for validation
class ChatbotRequest(BaseModel):
    user_name: str
    register_number: str
    email: str  # ✅ Added email for notifications
    subject: str
    description: str
    category: str  # "complaint" or "request"

@router.post("/generate-letter")
async def generate_formal_letter(request: ChatbotRequest):
    if request.category.lower() not in ["complaint", "request"]:
        raise HTTPException(status_code=400, detail="Invalid category. Must be 'complaint' or 'request'.")

    # ✅ Generate the formatted letter
    letter = generate_letter(request.user_name, request.register_number, request.subject, request.description)

    # ✅ Store in the correct MongoDB collection
    doc = {
        "user_name": request.user_name,
        "register_number": request.register_number,
        "email": request.email,  # ✅ Store email for future notifications
        "subject": request.subject,
        "description": request.description,
        "letter": letter,
        "created_at": datetime.utcnow(),
        "status": "pending"  # ✅ Default status
    }

    if request.category.lower() == "complaint":
        await complaints_collection.insert_one(doc)  # ✅ Store in complaints
    else:
        await requests_collection.insert_one(doc)  # ✅ Store in requests

    return {"letter": letter, "message": f"{request.category.capitalize()} stored successfully"}
