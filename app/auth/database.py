from app.auth.models import User

_users_db: dict[int, User] = {}
_next_id = 1

def seed():
    global _next_id
    ## lazy import
    from app.auth.service import hash_password
    _users_db[_next_id] = User(
        id=_next_id,
        username="user@test.com",
        password_hash=hash_password("password123")
    )
    _next_id += 1