from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DATABASE_NAME

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

# Collection for Todos
todo_collection = db.get_collection("todos")
