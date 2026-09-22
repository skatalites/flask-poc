from app.auth.database import _users_db
from app.auth.models import User

class UserRepository:
    def find_by_username(self, username: str) -> User | None:
        for user in _users_db.values():
            if user.username == username:
                return user
        return None

    def find_by_id(self, user_id: int) -> User | None:
        return _users_db.get(user_id)

    def save(self, user: User) -> User:
        _users_db[user.id] = user
        return user