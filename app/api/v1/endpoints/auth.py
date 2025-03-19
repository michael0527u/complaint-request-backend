from fastapi import APIRouter, HTTPException, Depends
from app.core.database import users_collection, check_connection
from app.core.security import hash_password, verify_password
from app.schemas.user_schemas import UserLoginSchema, UserRegisterSchema
import json

router = APIRouter(tags=["Auth"])  # ✅ Added tags at router level

@router.post("/register")
async def register(user: UserRegisterSchema):
    await check_connection()

    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    del user_data["confirm_password"]  # ✅ Remove confirm_password before storing

    try:
        result = await users_collection.insert_one(user_data)
        return {"message": "User registered successfully", "user_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

@router.post("/login")
async def login(user: UserLoginSchema):
    await check_connection()

    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
