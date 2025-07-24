from app.model.user import User
from bson import ObjectId


class UserRepository:
    def __init__(self, collection):
        self.collection = collection

    async def insert(self, user: User):
        return await self.collection.insert_one(user.to_dict())

    async def get_all(self):
        return await self.collection.find().to_list(length=None)

    async def get_by_id(self, user_id: str):
        return await self.collection.find_one({"_id": ObjectId(user_id)})

    async def update(self, user_id: str, user: User):
        return await self.collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user.to_dict()}
        )

    async def delete(self, user_id: str):
        return await self.collection.delete_one({"_id": ObjectId(user_id)})

    async def get_by_email(self, email: str):
        return await self.collection.find_one({"email": email})
