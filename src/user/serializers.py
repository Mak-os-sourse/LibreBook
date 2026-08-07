from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "is_active", "create_at", "is_superuser"]
        extra_kwargs = {'is_superuser': {'read_only': True}, 'is_active': {'read_only': True}}

class RegistUser(serializers.Serializer):
    name: str = serializers.CharField(max_length=100)
    email: str = serializers.EmailField()
    username: str = serializers.CharField(max_length=100)
    password: str = serializers.CharField(max_length=30)

class LoginUser(serializers.Serializer):
    field: str = serializers.CharField(max_length=100)
    password: str = serializers.CharField(max_length=30)
    
class TokenResponse(serializers.Serializer):
    access_token: str = serializers.CharField()
    token_type: str = serializers.CharField(default="bearer")
    expires_in: int = serializers.IntegerField()
