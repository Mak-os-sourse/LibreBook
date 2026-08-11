from rest_framework import serializers

from user.serializers import UserSerializer
from book.models import Book

class BookSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    photo = serializers.FileField(read_only=True)
    
    class Meta:
        model = Book
        fields = "__all__"
        
class UploadFile(serializers.Serializer):
    book_id: int = serializers.IntegerField()
    file = serializers.FileField()