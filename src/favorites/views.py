from django.db.models import F
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from favorites.serializers import FavoritesSerializers
from favorites.models import Favorites
from book.models import Book

class FavoritesMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    
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
        
        serializer.save(user=self.request.user)
    
    def perform_destroy(self, instance: FavoritesSerializers):
        book: Book = instance.book
        if book.count_favorites != 0:
            book.count_favorites = F("count_favorites") - 1
            book.save()
        return super().perform_destroy(instance)