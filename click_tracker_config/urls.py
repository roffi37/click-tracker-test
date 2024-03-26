from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tracker import views

router = DefaultRouter()
router.register(r"models", views.ModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
