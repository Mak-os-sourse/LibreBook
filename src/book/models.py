from django.db import models

class Book(models.Model):
    name: str = models.CharField(max_length=500)
    description: str = models.CharField(max_length=500)
    author: str = models.CharField(max_length=100)
    user_id: int = models.IntegerField()
    pub_date: int = models.DateTimeField()
    create_at: int = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_text