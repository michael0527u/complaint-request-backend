from pydantic import BaseModel

class Complaint(BaseModel):
    user_email: str
    subject: str
    description: str
    status: str = "Pending"
