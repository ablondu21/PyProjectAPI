from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from app.routes import task, user, group, auth
from app.auth.jwt_handler import verify_token

load_dotenv()

app = FastAPI()


@app.get("/")
def init():
    return {"message": "App is running"}


app.include_router(
    task.router, prefix="/tasks", tags=["Tasks"], dependencies=[Depends(verify_token)]
)
app.include_router(
    user.router, prefix="/users", tags=["Users"], dependencies=[Depends(verify_token)]
)
app.include_router(
    group.router,
    prefix="/groups",
    tags=["Groups"],
    dependencies=[Depends(verify_token)],
)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
