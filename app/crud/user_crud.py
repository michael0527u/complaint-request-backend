from app.core.database import db
from app.core.security import hash_password, verify_password, create_jwt_token

async def create_user(username: str, email: str, password: str):
    user = await db.users.find_one({"email": email})
    if user:
        return None  # Email already exists
    hashed_pwd = hash_password(password)
    await db.users.insert_one({"username": username, "email": email, "password": hashed_pwd})
    return create_jwt_token(email)

async def authenticate_user(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        return None
    return create_jwt_token(email)
