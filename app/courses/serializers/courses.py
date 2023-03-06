"""Courses serializers. """

# Django restframework
from rest_framework import serializers

# Django
from django.utils.text import slugify
import uuid

# Models
from courses.models.courses import Course

# Serializers
from users.serializers.users import UserModelSerializer
from courses.serializers.categories import CategoryModelSerializer

class CourseModelSerializer(serializers.ModelSerializer):
    """worldcup pool model serializer."""
    author = UserModelSerializer(read_only=True)
    category = CategoryModelSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        

class CreateCourseModelSerializer(serializers.ModelSerializer):
    """Course model serializer."""
    slug = serializers.SlugField()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnail = serializers.ImageField()

    class Meta:
        model = Course
        fields = '__all__'
  
    def validate(self, data):
        """Validate if de slug already exists. If exists modificate."""
        slug_name = data['slug']
        if Course.objects.filter(slug=slug_name).exists():
            course = Course.objects.filter(slug=slug_name)
            if course.slug.lower() == slug_name:
                raise serializers.ValidationError('Slug name already exists.')
            
        data['slug'] = slug_name.lower()
        return data
