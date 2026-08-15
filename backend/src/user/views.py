from rest_framework.request import Request
from rest_framework import status, filters, mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from settings import settings
from user.models import User
from user.security import token, authenticate, IsOwnerOrReadOnly
from user.serializers import RegistUser, LoginUser, TokenResponse, UserSerializer

@extend_schema(responses=TokenResponse)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_token(request: Request):
    access, refresh = token.create_tokens(id=request.user.id, username=request.user.username, email=request.user.email)
    res = Response(TokenResponse({"access_token": access, "expires_in": settings.jwt_access_exp}).data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema(request=RegistUser, responses=TokenResponse)
@api_view(["POST"])
def regist(request: Request):
    data = RegistUser(data=request.data)
    data.is_valid(raise_exception=True)
    
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
    res = Response(TokenResponse({"access_token": access, "expires_in": settings.jwt_access_exp}).data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema(request=LoginUser, responses=TokenResponse)
@api_view(["POST"])
def login(request: Request):
    data = LoginUser(data=request.data)
    data.is_valid(raise_exception=True)
    
    user = authenticate(
        request,
        field=data.validated_data.get("field"),
        password=data.validated_data.get("password")
    )
    if user is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    access, refresh = token.create_tokens(id=user.id, username=user.username, email=user.email)
    res = Response(TokenResponse({"access_token": access, "expires_in": settings.jwt_access_exp}).data)
    res.set_cookie("token", refresh, httponly=True)
    return res

@extend_schema(responses=UserSerializer)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_me(request: Request):
    res = Response(UserSerializer(request.user, read_only=True).data)
    return res

class UserMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["username", "email"]
    filterset_fields = ["username", "email", "id"]
    ordering_fields = "__all__"