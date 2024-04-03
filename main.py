from fastapi import FastAPI
from app.user.controllers.user_controller import router as user_router
app = FastAPI()

app.include_router(user_router, prefix="/users")
# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}