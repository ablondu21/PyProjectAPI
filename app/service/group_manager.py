from app.model.group import Group
from app.repository.group_repository import GroupRepository


class GroupService:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    async def create_group(self, group: Group):
        return await self.group_repository.insert(group)

    async def get_all_groups(self):
        return await self.group_repository.get_all()

    async def get_group_by_id(self, group_id: str):
        return await self.group_repository.get_by_id(group_id)

    async def update_group(self, group_id: str, group: Group):
        return await self.group_repository.update(group_id, group)

    async def delete_group(self, group_id: str):
        return await self.group_repository.delete(group_id)

    async def get_group_membersname(self, member_id: str):
        return await self.group_repository.get_group_by_member(member_id)
