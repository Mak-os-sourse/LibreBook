import magic
from pathlib import Path
from django.db.models import Subquery, OuterRef
from django.contrib.auth.models import AnonymousUser
from django.core.files import File
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from book.models import Book
from favorites.models import Favorites
from book.serializers import BookSerializers, UploadFile
from user.security import IsOwnerOrReadOnly

@extend_schema(request=UploadFile)
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def update_document(request: Request):
    data = UploadFile(data=request.data)
    data.is_valid(raise_exception=True)

    file: File = data.validated_data["file"]
    file_data = file.read()
    suffix = Path(file.name).suffix
    
    mime = magic.from_buffer(file_data, mime=True)
    if mime not in ["application/pdf"]:
        return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    
    try:
        book = Book.objects.get(id=data.validated_data["book_id"])
        book.document.save(f"book-document-{book.pk}{suffix}", file)
        return Response({"success": True})
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@extend_schema(request=UploadFile)
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def update_image(request: Request):
    data = UploadFile(data=request.data)
    data.is_valid(raise_exception=True)

    file: File = data.validated_data["file"]
    file_data = file.read()
    suffix = Path(file.name).suffix
    
    mime = magic.from_buffer(file_data, mime=True)
    if mime not in ["image/jpeg", "image/png", "image/webp", "image/svg"]:
        return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    
    try:
        book = Book.objects.get(id=data.validated_data["book_id"])
        book.photo.save(f"book-image-{book.pk}{suffix}", file)
        return Response({"success": True})
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

class BookMixin(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["name", "description", "author", "user_id", "pub_date", "create_at", "count_favorites"]
    filterset_fields = ["name", "description", "author", "user_id", "pub_date", "create_at", "count_favorites"]
    search_fields = ["name", "description", "author"]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return self.queryset
        
        return self.queryset.annotate(favorite_id=Subquery(
            Favorites.objects.filter(
                user=self.request.user,
                book=OuterRef("pk")
            ).values("id")[:1]
        ))