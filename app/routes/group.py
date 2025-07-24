from fastapi import APIRouter, HTTPException
from app.db.dbconn import db
from app.repository.group_repository import GroupRepository
from app.service.group_manager import GroupService
from app.model.group import Group
from app.schema.serializer import all_dict, individual_dict

router = APIRouter()

group_collection = db["group"]
group_repository = GroupRepository(group_collection)
group_service = GroupService(group_repository)


@router.post("/")
async def create_group(group: Group):
    await group_service.create_group(group)
    return {"message": "Group created"}


@router.get("/")
async def get_all_groups():
    data = await group_service.get_all_groups()
    return all_dict(data)


@router.get("/{group_id}")
async def get_group(group_id: str):
    data = await group_service.get_group_by_id(group_id)
    if not data:
        raise HTTPException(status_code=404, detail="Group not found")
    return individual_dict(data)


@router.put("/{group_id}")
async def update_group(group_id: str, group: Group):
    updated_group = await group_service.update_group(group_id, group)
    if not updated_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group updated"}


@router.delete("/{group_id}")
async def delete_group(group_id: str):
    deleted = await group_service.delete_group(group_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted"}


@router.get("/members/{member_id}")
async def get_group_members(member_id: str):
    groups = await group_service.get_group_membersname(member_id)
    if not groups:
        raise HTTPException(status_code=404, detail="No groups found for this member")
    return all_dict(groups)
