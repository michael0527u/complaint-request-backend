from pydantic import BaseModel, EmailStr, field_validator

class UserRegisterSchema(BaseModel):
    username: str
    register_number: str
    phone_number: str
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseModel):
    _id: str  # ✅ MongoDB uses ObjectId
    username: str
    register_number: str
    phone_number: str
    email: EmailStr

    class Config:
        from_attributes = True  # ✅ Correct for Pydantic v2

