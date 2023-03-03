"""Courses model."""

# Django
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
import uuid

# Models
from courses.models.categories import Category
from users.models.users import User

class Course(models.Model):
    """Course model."""
    title = models.CharField(max_length=255, verbose_name='Course Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Course Slug')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category')
    description = models.TextField(max_length=450, blank=True, verbose_name="Brand descrition")
    thumbnail = models.ImageField(upload_to='media/courses/thumbnail/', default='media/courses/thumbnail/default.jpg', verbose_name='Course thumbnail')
    video = models.FileField(upload_to='media/courses/videos/', blank=True, null=True, verbose_name= 'Course Video')
    video_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Course Video Url')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_user')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["-created_at"]


@receiver(models.signals.pre_save, sender=Course)
def set_slug(sender, instance, **kwargs):
    """Create new Course slug if slug exists."""
    if Course.objects.filter(slug=instance.slug).exists():
        id = str(uuid.uuid4())
        new_slug = slugify("{}-{}".format(instance.title, id[:8]))
        instance.slug = new_slug

@receiver(models.signals.post_delete, sender=Course)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Course` object is deleted.
    """
    if instance.video:
        instance.video.delete(False)