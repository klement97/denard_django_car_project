from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from seller.models import Seller


class CarTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='Tester')
        user.set_password('test123')
        user.save()
        self.client.login(username=user.username, password='test123')

        self.seller = Seller.objects.create(name='Tommy', country='albania', city='tirana', address='12345')

    def test_car_create(self):
        url = reverse('new')
        data = {
            'brand': 'Mercedez',
            'model': 's500',
            'year': 2005,
            'seller': self.seller.id
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
