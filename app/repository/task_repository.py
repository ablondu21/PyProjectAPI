from app.model.task import Task
from bson import ObjectId


class TaskRepository:

    def __init__(self, collection):
        self.collection = collection

    async def insert(self, task: Task):
        return await self.collection.insert_one(task.to_dict())

    async def get_all(self):
        return await self.collection.find().to_list(length=None)

    async def get_by_id(self, task_id: str):
        return await self.collection.find_one({"_id": ObjectId(task_id)})

    async def update(self, task_id: str, task: Task):
        return await self.collection.update_one(
            {"_id": ObjectId(task_id)}, {"$set": task.to_dict()}
        )

    async def delete(self, task_id: str):
        return await self.collection.delete_one({"_id": ObjectId(task_id)})
