from app.model.group import Group
from bson import ObjectId


class GroupRepository:
    def __init__(self, collection):
        self.collection = collection

    async def insert(self, group: Group):
        return await self.collection.insert_one(group.to_dict())

    async def get_all(self):
        return await self.collection.find().to_list(length=None)

    async def get_by_id(self, group_id: str):
        return await self.collection.find_one({"_id": ObjectId(group_id)})

    async def update(self, group_id: str, group: Group):
        return await self.collection.update_one(
            {"_id": ObjectId(group_id)}, {"$set": group.to_dict()}
        )

    async def delete(self, group_id: str):
        return await self.collection.delete_one({"_id": ObjectId(group_id)})

    async def get_group_by_member(self, member_id: str):
        return await self.collection.find({"members": member_id}).to_list(length=None)
