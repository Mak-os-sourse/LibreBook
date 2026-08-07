from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from user import views as user_views
from book import views as book_views

router = SimpleRouter()
router.register("user", user_views.UserMixin, basename="user")
router.register("book", book_views.BookMixin, basename="book")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    
    path('api/', include(router.urls)),
    path("api/user/login", user_views.login, name="login"),
    path("api/user/regist", user_views.regist, name="regist"),
    path("api/user/update-token", user_views.update_token, name="update-token"),
    path("api/user/get/me", user_views.get_me, name="me"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
