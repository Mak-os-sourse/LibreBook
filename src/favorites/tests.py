from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse

from favorites.models import Favorites
from book.models import Book

client = APIClient()

class FavoritesMixinTestCase(TestCase):
    def test_creat(self):
        res = client.post(reverse("book-list"))
        
        data = res.json()
        self.assertTrue(res.status_code == 201)
        self.assertTrue(Book.objects.filter(id=data["id"]).exists())