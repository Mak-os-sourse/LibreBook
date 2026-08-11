from rest_framework import serializers

from favorites.models import Favorites
from book.models import Book
from user.serializers import UserSerializer

class FavoritesSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    class Meta:
        model = Favorites
        fields = "__all__"