"""Courses Urls."""

# Django rest framework
from rest_framework.routers import DefaultRouter

#Django
from django.urls import path, include

# Views
from .views import categories as category_views
from .views import courses as courses_views

router = DefaultRouter()
router.register(r'categories', category_views.CategoryViewSet, basename="category")
router.register(r'courses', courses_views.CourseViewSet, basename="courses")

urlpatterns = [
    path('', include(router.urls))
]