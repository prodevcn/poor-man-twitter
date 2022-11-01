from django.contrib import admin
from django.urls import path, include
from tweets import views
from rest_framework import routers
from .views import TweetSerializer, TweetViewSet

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
