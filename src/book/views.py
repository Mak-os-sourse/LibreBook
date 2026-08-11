import magic
from pathlib import Path
from django.core.files import File
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from book.models import Book
from book.serializers import BookSerializers, UploadFile

@extend_schema(request=UploadFile)
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def update_image(request: Request):
    data = UploadFile(data=request.data)
    
    if not data.is_valid():
        return Response(data.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

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
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["name", "description", "author", "user_id", "pub_date", "create_at"]
    filterset_fields = ["name", "description", "author", "user_id", "pub_date", "create_at"]
    search_fields = ["name", "description", "author"]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)