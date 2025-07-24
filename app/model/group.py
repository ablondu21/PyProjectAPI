from pydantic import BaseModel
from typing import List


class Group(BaseModel):
    name: str
    description: str
    members: List[str]

    def to_dict(self):
        return self.dict()
