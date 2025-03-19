from app.db.database import complaints_collection
from bson import ObjectId

async def create_complaint(complaint_data):
    complaint_dict = complaint_data.dict()
    result = await complaints_collection.insert_one(complaint_dict)
    complaint_dict["_id"] = str(result.inserted_id)
    return complaint_dict

async def get_all_complaints():
    complaints = await complaints_collection.find().to_list(None)
    for complaint in complaints:
        complaint["_id"] = str(complaint["_id"])
    return complaints
