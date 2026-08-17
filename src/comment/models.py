from django.db import models

from book.models import Book
from user.models import User

class Comment(models.Model):
    content: str = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_at: int = models.DateTimeField(auto_now_add=True)