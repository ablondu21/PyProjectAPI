from app.model.user import User
from app.repository.user_repository import UserRepository
from app.auth.function import hash_password


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user: User):
        user.password = hash_password(user.password)
        return await self.user_repository.insert(user)

    async def get_all_users(self):
        return await self.user_repository.get_all()

    async def get_user_by_id(self, user_id: str):
        return await self.user_repository.get_by_id(user_id)

    async def update_user(self, user_id: str, user: User):
        return await self.user_repository.update(user_id, user)

    async def delete_user(self, user_id: str):
        return await self.user_repository.delete(user_id)

    async def get_user_by_email(self, email: str):
        return await self.user_repository.get_by_email(email)
