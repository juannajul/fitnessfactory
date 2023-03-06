"""Courses views."""

# Django rest framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Serializers
from courses.serializers.courses import CourseModelSerializer,CreateCourseModelSerializer

# Models 
from courses.models.courses import Course

# Pagination

class CourseViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """Courses view set"""

    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        """Return serializer based on actions"""
        if self.action == 'create':
            return CreateCourseModelSerializer
        return CourseModelSerializer
