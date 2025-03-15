from fastapi import APIRouter, HTTPException
from models import Todo, TodoResponse
from database import todo_collection
from bson import ObjectId
from typing import List

router = APIRouter()

# 🚀 Create a new To-Do
@router.post("/todos", response_model=dict)
async def create_todo(todo: Todo):
    new_todo = await todo_collection.insert_one(todo.dict())
    return {"id": str(new_todo.inserted_id)}

# 📌 Get all To-Dos
@router.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    todos = await todo_collection.find().to_list(100)
    return [{"id": str(todo["_id"]), **todo} for todo in todos]

# ✅ Update a To-Do
@router.put("/todos/{todo_id}", response_model=dict)
async def update_todo(todo_id: str, todo: Todo):
    result = await todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": todo.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo updated"}

# ❌ Delete a To-Do
@router.delete("/todos/{todo_id}", response_model=dict)
async def delete_todo(todo_id: str):
    result = await todo_collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
