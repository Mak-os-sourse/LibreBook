from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from faker import Faker

from user.security.token import token
from user.utils import add_user, add_user_fake_data
from user.serializers import RegistUser, LoginUser

faker = Faker()
client = APIClient()

class UserTestCase(TestCase):
    def test_regist(self):
        res = client.post(reverse("regist"),
            data=RegistUser(
                add_user_fake_data()
            ).data
        )
        
        result = res.json()
        self.assertTrue(res.status_code == 200)
        self.assertTrue(result["access_token"])
        self.assertTrue(result["token_type"] == "bearer")
        self.assertTrue(res.cookies.get("token") is not None)
    
    def test_login(self):
        password = faker.password()
        user = add_user(password)
        
        res = client.post(reverse("login"),
            data=LoginUser(
                {
                    "field": user.email,
                    "password": password,
                }
            ).data
        )
        
        result = res.json()
        
        self.assertTrue(res.status_code == 200)
        self.assertTrue(result["access_token"])
        self.assertTrue(result["token_type"] == "bearer")
        self.assertTrue(res.cookies.get("token") is not None)
    
    def test_update_token(self):
        user = add_user()
        access, _ = token.create_tokens(id=user.id, username=user.username, email=user.email)
        
        res = client.post(reverse("update-token"),
            HTTP_AUTHORIZATION=f"Bearer {access}",
        )
        
        
        result = res.json()

        self.assertTrue(res.status_code == 200)
        self.assertTrue(result["access_token"])
        self.assertTrue(result["token_type"] == "bearer")
        self.assertTrue(res.cookies.get("token") is not None)
    
    def test_get_me(self):
        user = add_user()
        
        client.force_authenticate(user)
        
        res = client.get(reverse("me"))
        
        result = res.json()
        
        self.assertTrue(res.status_code == 200)
        self.assertTrue(result["id"] == user.id)