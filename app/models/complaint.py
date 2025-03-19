from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComplaintCreate(BaseModel):
    user_id: str
    type: str  # 'complaint' or 'request'
    subject: str
    description: str

class ComplaintResponse(BaseModel):
    id: str
    user_id: str
    type: str
    subject: str
    description: str
    letter: str
    created_at: datetime
