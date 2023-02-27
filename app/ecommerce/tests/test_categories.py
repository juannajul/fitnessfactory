from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, CoreAPIClient

# Models
from ecommerce.models.categories import Category

# Serializers 
from ecommerce.serializers.categories import CategoryModelSerializer

class CreateCategoryTest(APITestCase):
    def test_create_category(self):
        response = self.client.post(reverse('ecommerce:category-list'), data={
            'name':'Ropa',
            'slug': 'ropa',
            'is_active': True
        })
        category = Category.objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['name'], category.name)
        self.assertEqual(response.data['slug'], category.slug)
        self.assertTrue(response.data['is_active'], category.is_active)


class ReadCategotyTest(APITestCase):
    def setUp(self):
        """Test case setup."""
        self.category_1 = Category.objects.create(
            name='Franelas',
            slug='franelas',
            is_active=True
        )
        self.category_2 = Category.objects.create(
            name='Accesorios',
            slug='accesorios',
            is_active=True
        )
    
    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(reverse('ecommerce:category-list'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        
    def test_list_categories(self):
        response = self.client.get(reverse('ecommerce:category-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print(response)

    def test_retrieve_category(self):
        response = self.client.get(reverse('ecommerce:category-detail', args=[self.category_1.slug]))
        category = Category.objects.get(slug=self.category_1.slug)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['name'], category.name)
        self.assertEqual(response.data['slug'], category.slug)
        self.assertTrue(response.data['is_active'], category.is_active)

class UpdateCategoryTest(APITestCase):
    def setUp(self):
        """Test case setup."""
        self.category = Category.objects.create(
            name = 'Franelas',
            slug = 'franelas',
            is_active = True
        )
        self.data = {
            'name': 'Ropa',
            'slug': 'ropa',
            'is_active': False
        }

    def test_update_category(self):
        response = self.client.put(reverse('ecommerce:category-detail', args=[self.category.slug]), self.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['slug'], self.data['slug'])
        self.assertFalse(response.data['is_active'], self.data['is_active'])
        self.assertNotEqual(response.data['name'], self.category.name)
        self.assertNotEqual(response.data['slug'], self.category.slug)
        self.assertNotEqual(response.data['is_active'], self.category.is_active)

class DeleteCategoryTest(APITestCase):
    def setUp(self):
        """Test case setup."""
        self.category = Category.objects.create(
            name = 'Franelas',
            slug = 'franelas',
            is_active = True
        )
    def test_delete_category(self):
        response = self.client.delete(reverse('ecommerce:category-detail', args=[self.category.slug]))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)        
        