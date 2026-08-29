from rest_framework import serializers

from book.models import Book
from favorites.models import Favorites
from book.serializers import BookSerializers

class FavoritesSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    class Meta:
        model = Favorites
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["book"] = BookSerializers(instance.book).data
        return representation