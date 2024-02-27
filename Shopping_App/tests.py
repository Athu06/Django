# tests.py
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Product, User, Recommendation

class ProductAPITest(APITestCase):
    def test_create_product(self):
        url = '/products/'
        data = {'shape': 'circle', 'size': 'medium', 'location': 'A', 'price': 20.0}
        response = self.client.post(url, data, format='json')


class UserAPITest(APITestCase):
    def test_create_user(self):
        url = '/users/'
        data = {'name': 'John Doe', 'age': 25, 'address': '123 Main St'}
        response = self.client.post(url, data, format='json')


class RecommendationAPITest(APITestCase):
    def test_create_recommendation(self):
        product = Product.objects.create(shape='circle', size='medium', location='A', price=20.0)
        user = User.objects.create(name='John Doe', age=25, address='123 Main St')

        url = '/recommendations/'
        data = {'product': product.id, 'user': user.id}
        response = self.client.post(url, data, format='json')

