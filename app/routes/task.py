from fastapi import APIRouter, HTTPException
from app.db.dbconn import db
from app.repository.task_repository import TaskRepository
from app.service.task_manager import TaskService
from app.model.task import Task
from app.schema.serializer import all_dict, individual_dict


router = APIRouter()

task_collection = db["task"]

repo = TaskRepository(task_collection)

service = TaskService(repo)


@router.post("/")
async def create_task(task: Task):
    await service.create_task(task)
    return {"message": "Task created"}


@router.get("/")
async def get_all_tasks():
    data = await service.get_all_tasks()
    return all_dict(data)


@router.get("/{task_id}")
async def get_task(task_id: str):
    task = await service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return individual_dict(task)


@router.put("/{task_id}")
async def update_task(task_id: str, task: Task):
    result = await service.update_task(task_id, task)
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Task not found or not modified")
    return {"message": "Task updated"}


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    result = await service.delete_task(task_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
