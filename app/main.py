from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.chatbot import router as chatbot_router
from app.api.v1.endpoints.complaints import router as complaints_router
from app.core.database import check_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Complaint & Request API")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ensure correct routers are included
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(chatbot_router, prefix="/api/v1/chatbot", tags=["Chatbot"])
app.include_router(complaints_router, prefix="/api/v1/complaints", tags=["Complaints"])

# ✅ Check MongoDB connection at startup
@app.on_event("startup")
async def startup_event():
    await check_connection()

@app.get("/")
async def root():
    return {"message": "Complaint & Request Raising System API is running!"}
