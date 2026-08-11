import jwt
import time
import jwt
from typing import Any
from django.contrib.auth.models import AnonymousUser
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from drf_spectacular.authentication import TokenScheme
from drf_spectacular.plumbing import build_bearer_security_scheme_object

from settings import settings
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

class JWTScheme(TokenScheme):
    target_class = 'user.auth.JWTAuthentication'
    name = "JWTScheme"
    
    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )
        
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

class Token:
    def create_tokens(self, id: int,  username: str, email: str) -> tuple[str, str]:
        """Use refresh, access = token.create(...)"""
        now = int(time.time())
        refresh_exp = now + settings.jwt_refresh_exp
        access_exp = now + settings.jwt_access_exp
        
        refresh = self.encode(id, username, email, exp=refresh_exp)
        access = self.encode(id, username, email, exp=access_exp)
        return refresh, access
    
    def encode(self, id: int, username: str, email: str, exp: int) -> str:
        return jwt.encode(
            {
                "id": id,
                "username": username,
                "email": email,
                "exp": exp,
            },
            key=settings.jwt_key,
            algorithm=settings.jwt_algorithm,
        )
    
    def decode(self, token: str, verify_exp: bool = True) -> dict[Any, Any]:
        return jwt.decode(
            token,
            key=settings.jwt_key,
            algorithms=settings.jwt_algorithm,
            options={"verify_exp": verify_exp}
        )
        
token = Token()