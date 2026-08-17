from rest_framework import serializers

from user.serializers import UserSerializer
from book.models import Book

class BookSerializers(serializers.ModelSerializer):
    name: str = serializers.CharField(min_length=4)
    user = UserSerializer(default=serializers.CurrentUserDefault(), read_only=True)
    photo = serializers.FileField(read_only=True)
    count_favorites = serializers.IntegerField(read_only=True)
    in_favorite: bool = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Book
        fields = "__all__"
        
class UploadFile(serializers.Serializer):
    book_id: int = serializers.IntegerField()
    file = serializers.FileField()