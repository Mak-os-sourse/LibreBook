from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse

from favorites.models import Favorites
from book.utils import add_book
from book.models import Book

client = APIClient()

class FavoritesMixinTestCase(TestCase):
    def test_creat(self):
        book = add_book()
        
        client.force_authenticate(book.user)
        res = client.post(reverse("favorites-list"),
            data={
                "book": book.id,
            }
        )
        
        result = res.json()
        
        self.assertTrue(res.status_code == 201)
        self.assertTrue(Favorites.objects.filter(id=result["id"]).exists())
        self.assertTrue(Book.objects.get().count_favorites > 0)
        
    def test_delete(self):
        book = add_book()
        model = Favorites(book=book, user=book.user)
        model.save()
        
        client.force_authenticate(book.user)
        res = client.delete(reverse("favorites-detail", kwargs={"pk": model.id}))
        
        self.assertTrue(res.status_code == 204)
        self.assertTrue(not Favorites.objects.filter(id=model.id).exists())
        self.assertTrue(Book.objects.get().count_favorites == 0)