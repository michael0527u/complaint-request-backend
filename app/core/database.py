import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "complaintsdb"

# ✅ Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
database = client[DB_NAME]

# ✅ Define collections
users_collection = database["users"]
complaints_collection = database["complaints"]  # ✅ Stores complaints
requests_collection = database["requests"]  # ✅ Stores requests

async def check_connection():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB connection is active")
    except Exception as e:
        print(f"❌ MongoDB connection error: {e}")
