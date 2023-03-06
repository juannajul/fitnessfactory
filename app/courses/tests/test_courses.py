import io
import os
from PIL import Image

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# Models
from courses.models.categories import Category
from courses.models.courses import Course
from users.models.users import User
    # title = models.CharField(max_length=255, verbose_name='Course Title')
    # slug = models.SlugField(max_length=255, unique=True, verbose_name='Course Slug')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category')
    # description = models.TextField(max_length=450, blank=True, verbose_name="Brand descrition")
    # thumbnail = models.ImageField(upload_to='media/courses/thumbnail/', default='media/courses/thumbnail/default.jpg', verbose_name='Course thumbnail')
    # video = models.FileField(upload_to='media/courses/videos/', blank=True, null=True, verbose_name= 'Course Video')
    # video_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Course Video Url')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_user')
    # created_at = models.DateTimeField(auto_now_add=True)
    # is_active = models.BooleanField(default=True)

PASSWORD = 'pAssw0rd!'

class CreateCourseTest(APITestCase):
    def generate_thumbnail_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(155, 155), color=(155,55,0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    
    def setUp(self):
        """Test case setup."""
        self.category = Category.objects.create(
            name='Training',
            slug='training',
            is_active=True
        )
        self.user = User.objects.create_user(
            username= 'useert',
            email= 'juan@gmail.com',
            first_name= 'Test',
            last_name= 'User',
            password= PASSWORD,
        )

        self.user.save()
        login_user_response = self.client.post(reverse('users:users-login'), data={
            'email': self.user.email,
            'password': PASSWORD,
        })

        self.access_token = login_user_response.data['access_token']
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.access_token)}

        self.data = {
            'title':'training 1',
            'slug': 'training-1',
            'category': self.category.pk,
            'description': 'Course description.',
            'thumbnail': self.generate_thumbnail_file(),
            'video_url': 'https://www.youtube.com/watch?v=Rr1-UTFCuH4',
            'is_active': True
        }

    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(reverse('courses:courses-list'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        response = self.client.post(reverse('courses:courses-list'), data=self.data, **self.header)
        course = Course.objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['title'], course.title)
        self.assertEqual(response.data['slug'], course.slug)
        self.assertEqual(response.data['category'], course.category.pk)
        #self.assertEqual(response.data['thumbnail'], course.thumbnail)
        self.assertEqual(response.data['video_url'], course.video_url)
        self.assertEqual(self.user, course.author)
        self.assertTrue(response.data['is_active'], course.is_active)
