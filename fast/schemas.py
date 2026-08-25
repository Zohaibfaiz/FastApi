from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str
    assign_to: str
    category: str
    custom_category: Optional[str] = None

    timeframe: str
    custom_timeframe: Optional[str] = None
    priority: str
   
class TaskResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)