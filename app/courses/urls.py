"""Courses Urls."""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]