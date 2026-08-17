from faker import Faker
from typing import Any

from user.models import User
from book.models import Book
from user.utils import add_user

faker = Faker()

def add_book(user: User | None = None) -> Book:
    user_data = add_user() if user is None else user
    book = Book(**add_book_fake_data(), user=user_data)
    book.save()
    return book

def add_book_fake_data() -> dict[str, Any]:
    return {
        "name": faker.name(),
        "author": faker.name(),
        "description": faker.text()
    }