from fastapi import APIRouter, HTTPException
from app.db.dbconn import db
from app.repository.user_repository import UserRepository
from app.service.user_manager import UserService
from app.model.user import User
from app.auth.function import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter()

user_collection = db["user"]
user_repository = UserRepository(user_collection)
user_service = UserService(user_repository)


@router.post("/login")
async def login(user: User):
    user_data = await user_service.get_user_by_email(user.email)

    if not user_data:
        raise HTTPException(status_code=400, detail="Email inexistent")

    if not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=400, detail="Parolă incorectă")

    access_token = create_access_token(data={"sub": user_data["email"]})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
async def create_user(user: User):
    await user_service.create_user(user)
    return {"message": "User created"}
