from typing import Optional
from datetime import datetime
from pydantic import BaseModel   

class ToDoCreate(BaseModel):
    task_title: str 
    description: Optional[str] = None
    task_completed: bool = False
    
class ToDoResponse(BaseModel):
    id: str
    task_title: str 
    description: Optional[str]
    created_at: datetime 
    task_completed: Optional[bool] = False
    
    class Config:
        from_attributes = True
