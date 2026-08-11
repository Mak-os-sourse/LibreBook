from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from comment.serializers import CommentSerializers
from comment.models import Comment

class CommentMixin(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = "__all__"
    search_fields = "__all__"
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)