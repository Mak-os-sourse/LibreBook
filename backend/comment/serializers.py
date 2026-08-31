from rest_framework import serializers

from user.serializers import UserSerializer
from comment.models import Comment
from book.models import Book

class CommentSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    up_votes: int = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Comment
        fields = "__all__"