from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend 

from book.models import Book
from book.serializers import BookSerializers

class BookMixin(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = "__all__"
    filterset_fields = "__all__"