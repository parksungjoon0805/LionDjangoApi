from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.urls import include, path
from rest_framework.test import APIClient
from rest_framework.routers import DefaultRouter
from .models import Product
from .views import ProductViewSet

class ProductViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        router = DefaultRouter()
        router.register(r'products', ProductViewSet)
        self.client.urls = [
            path('', include(router.urls)),
        ]

    def test_list(self):
        Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            price=100,
            in_stock=True
        )
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Product')

    def test_create(self):
        data = {
            'name': 'New Product',
            'description': 'This is a new product.',
            'price': '200.00',
            'in_stock': True
        }
        response = self.client.post(reverse('product-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'New Product')


    def test_get_product(self):
        """
        제품 목록을 가져오고 결과를 검증합니다.
        """
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)