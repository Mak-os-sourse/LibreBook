from django.db.models import F
from django.db.utils import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from favorites.serializers import FavoritesSerializers
from user.security import IsOwnerOrReadOnly
from favorites.models import Favorites
from book.models import Book

class FavoritesMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializers
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = "__all__"
    search_fields = "__all__"
    
    def perform_create(self, serializer: FavoritesSerializers):
        book: Book = serializer.validated_data["book"]
        book.count_favorites = F("count_favorites") + 1
        book.save()
        
        try:
            serializer.save(user=self.request.user)
        except IntegrityError as e:
            raise ValidationError(str(e))
    
    def perform_destroy(self, instance: FavoritesSerializers):
        book: Book = instance.book
        if book.count_favorites != 0:
            book.count_favorites = F("count_favorites") - 1
            book.save()
        return super().perform_destroy(instance)