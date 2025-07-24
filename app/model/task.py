from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Literal


class Task(BaseModel):
    group_id: str
    creator: str
    assignees: List[str]
    title: str
    description: str
    tip: Literal["to do", "doing", "done"]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def to_dict(self):
        return self.dict()
