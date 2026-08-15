from django.db import models
from user.models import User

class Book(models.Model):
    name: str = models.CharField(max_length=4, max_length=50)
    description: str = models.CharField(max_length=500, null=True)
    author: str = models.CharField(max_length=100)
    user: int = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date: int = models.DateTimeField(auto_now=True)
    create_at: int = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to="books")
    count_favorites: int = models.IntegerField(default=0)
    
    def __str__(self):
        return self.book_text