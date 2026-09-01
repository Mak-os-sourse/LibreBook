from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from user import views as user_views
from book import views as book_views
from comment import views as comment_views
from favorites import views as favorites_views
from django.views.static import serve

router = SimpleRouter()
router.register("user", user_views.UserMixin, basename="user")
router.register("book", book_views.BookMixin, basename="book")
router.register("comment", comment_views.CommentMixin, basename="comment")
router.register("favorites", favorites_views.FavoritesMixin, basename="favorites")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    
    path("", TemplateView.as_view(template_name="index.html")),
    path("regist", TemplateView.as_view(template_name="regist.html")),
    path("login", TemplateView.as_view(template_name="login.html")),
    path("add-book", TemplateView.as_view(template_name="addBook.html")),
    path("book", TemplateView.as_view(template_name="bookView.html")),
    path("profile", TemplateView.as_view(template_name="profile.html")),
    
    path("api/", include(router.urls)),
    
    path("api/book/update-image", book_views.update_image, name="update-book-image"),
    path("api/book/update-document", book_views.update_document, name="update-book-document"),
    
    path("api/user/login", user_views.login, name="login"),
    path("api/user/regist", user_views.regist, name="regist"),
    path("api/user/update-token", user_views.update_token, name="update-token"),
    path("api/user/get/me", user_views.get_me, name="me"),
    
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]