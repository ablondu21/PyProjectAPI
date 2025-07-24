from app.model.task import Task
from app.repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def create_task(self, task: Task):
        return await self.repository.insert(task)

    async def get_all_tasks(self):
        return await self.repository.get_all()

    async def get_task_by_id(self, task_id: str):
        return await self.repository.get_by_id(task_id)

    async def update_task(self, task_id: str, task: Task):
        return await self.repository.update(task_id, task)

    async def delete_task(self, task_id: str):
        return await self.repository.delete(task_id)
