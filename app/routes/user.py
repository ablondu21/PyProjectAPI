from fastapi import APIRouter, HTTPException
from app.db.dbconn import db
from app.repository.user_repository import UserRepository
from app.service.user_manager import UserService
from app.model.user import User
from app.schema.serializer import all_dict, individual_dict


router = APIRouter()

user_collection = db["user"]
user_repository = UserRepository(user_collection)
user_service = UserService(user_repository)


@router.get("/")
async def get_all_users():
    data = await user_service.get_all_users()
    return all_dict(data)

 
@router.get("/{user_id}")
async def get_user(user_id: str):
    data = await user_service.get_user_by_id(user_id)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return individual_dict(data)


@router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    await user_service.update_user(user_id, user)
    return {"message": "User updated"}


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    result = await user_service.delete_user(user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
