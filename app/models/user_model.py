from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    register_number: str
    phone_number: str
    password: str
    confirm_password: str

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    register_number: str
    phone_number: str
