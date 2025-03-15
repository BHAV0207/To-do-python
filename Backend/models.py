from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoResponse(Todo):
    id: str