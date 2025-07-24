from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str

    def to_dict(self):
        return self.dict()
