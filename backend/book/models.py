from django.db import models
from user.models import User

class Book(models.Model):
    name: str = models.CharField(max_length=50)
    description: str = models.CharField(max_length=500, null=True)
    author: str = models.CharField(max_length=100)
    user: int = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date: int = models.DateTimeField(auto_now=True)
    create_at: int = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="books", null=True)
    document = models.FileField(upload_to="books", null=True)
    count_favorites: int = models.IntegerField(default=0)
    