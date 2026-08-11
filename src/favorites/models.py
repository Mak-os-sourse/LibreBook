from django.db import models

from book.models import Book
from user.models import User

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_at: int = models.DateTimeField(auto_now_add=True)