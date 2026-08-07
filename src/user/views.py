from django.http import HttpRequest
from rest_framework import status, filters
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate

from settings import settings
from user.models import User
from user.auth import token, JWTAuthentication
from user.serializers import RegistUser, LoginUser, TokenResponse, UserSerializer

@extend_schema(responses=TokenResponse)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_token(request: HttpRequest):
    access, refresh = token.create_tokens(id=request.user.id, username=request.user.username, email=request.user.email)
    res = Response(TokenResponse(data={"access_token": access, "expires_in": settings.jwt_access_exp}).initial_data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema(request=RegistUser, responses=TokenResponse)
@api_view(["POST"])
def regist(request: HttpRequest):
    data = RegistUser(data=request.data)
    if not data.is_valid():
        return Response(data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    user = authenticate(
        request,
        field=data.validated_data.get("username"),
        password=data.validated_data.get("username")
    )
    if user is not None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    user = User(**data.validated_data)
    user.set_password(data.validated_data["password"])
    user.save()
    
    access, refresh = token.create_tokens(id=user.id, username=user.username, email=user.email)
    res = Response(TokenResponse(data={"access_token": access, "expires_in": settings.jwt_access_exp}).initial_data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema(responses=UserSerializer)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_me(request: HttpRequest):
    res = Response(UserSerializer(request.user, read_only=True).data)
    return res

@extend_schema(request=LoginUser, responses=TokenResponse)
@api_view(["POST"])
def login(request: HttpRequest):
    data = LoginUser(data=request.data)
    if not data.is_valid():
        return Response(data=data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    user = authenticate(
        request,
        field=data.validated_data.get("field"),
        password=data.validated_data.get("password")
    )
    if user is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    access, refresh = token.create_tokens(id=user.id, username=user.username, email=user.email)
    res = Response(TokenResponse(data={"access_token": access, "expires_in": settings.jwt_access_exp}).initial_data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema_view(
    list=extend_schema(responses=[UserSerializer]),
)
class UserMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["username", "email"]
    filterset_fields = ["username", "email", "id"]