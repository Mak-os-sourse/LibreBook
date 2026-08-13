from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework import status

from user.security.token import token
from user.models import User

def authenticate(request, field: str, password: str):
    try:
        data = {"username": field}
        if len(field.split("@")) == 2:
            data = {"email": field}
        user = User.objects.get(**data)
    except User.DoesNotExist:
        return None
    
    if user.check_password(password):
        return user
    else:
        return None

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        data = request.headers.get("Authorization")
        if data is None:
            request.user = AnonymousUser()
            return
        if not data.startswith("Bearer "):
            raise AuthenticationFailed("Error must be a bearer token", status.HTTP_401_UNAUTHORIZED)
        
        try:
            access = data.removeprefix("Bearer ")
            access_data = token.decode(access)
            user = User.objects.get(id=access_data["id"])
            request.user = user
            return user, access
        except:
            raise AuthenticationFailed("Error authenticate", status.HTTP_401_UNAUTHORIZED)