from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name: str = models.CharField()
    email: str = models.EmailField(unique=True)
    create_at: int = models.DateTimeField(auto_now=True)
    
    last_login = None
    first_name = None
    last_name = None
    date_joined = None