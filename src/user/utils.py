from faker import Faker
from typing import Any

from user.models import User

faker = Faker()

def add_user(password: str | None = None) -> User:
    data = add_user_fake_data()
    user = User(**data)
    user.set_password(data["password"] if password is None else password)
    user.save()
    return user
    
def add_user_fake_data() -> dict[str, Any]:
    return {
        "name": faker.name(),
        "email": faker.email(),
        "username": faker.user_name(),
        "password": faker.password(),
    }