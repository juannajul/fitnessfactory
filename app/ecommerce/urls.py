"""Ecommerce Urls."""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views


router = DefaultRouter()
#router.register(r'teams', teams_views.TeamViewSet, basename='teams')


urlpatterns = [
    path('', include(router.urls))
]