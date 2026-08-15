import tempfile
from rest_framework.test import APIClient
from django.test import TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

from book.utils import add_book

faker = Faker()
client = APIClient()

@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class BookTestCase(TestCase):
    def test_upload_file(self):
        book = add_book()
        client.force_authenticate(book.user)
        
        file = open("src/book/tests/test.jpeg", "rb")
        content = {"file": file, "book_id": book.id}
        
        res = client.post(reverse("update-book-image"), content, format="multipart")
        
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(result["success"])
    
    def test_upload_file_error(self):
            book = add_book()
            client.force_authenticate(book.user)
            
            file = SimpleUploadedFile("test.jpeg", b"Hello world!", content_type="image/jpeg")
            content = {"file": file, "book_id": book.id}
            
            res = client.post(reverse("update-book-image"), content, format="multipart")
            
            self.assertTrue(res.status_code == 415)