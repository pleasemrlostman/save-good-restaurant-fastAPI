from app.database import Database
from app.user.models.user import User
from typing import List


class UserService:
    def __init__(self):
        self.db = Database("save-good-restaurant").get_database()
        self.collection = self.db["users"]

    def get_user(self, user_id: str):
        return self.collection.find_one({"_id": user_id})

    def create_user(self, user: User):
        user_dict = user.dict()
        result = self.collection.insert_one(user_dict)
        return str(result.inserted_id)

    def get_all_users(self) -> List[User]:
        users = []
        for user in self.collection.find():
            users.append(User(**user))
        return users