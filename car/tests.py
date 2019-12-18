from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from car.models import Car
from seller.models import Seller


class CarTest(TestCase):
    fixtures = ['car', 'seller', 'user']

    def setUp(self):
        self.client = Client()
        user = User.objects.first()
        user.set_password('test')
        user.save()
        self.seller = Seller.objects.create(name='tomi', country='land', city='somewhere', address='bul1')
        self.seller.save()
        self.car = Car.objects.create(brand='ford', model='focus', year='2000', seller=self.seller)
        self.car.save()
        self.client.login(username=user.username, password='test')

    def test_car_list_view(self):
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEquals(len(self.databases), 1)
        self.assertEquals(response.status_code, 200)

    def test_car_create(self):
        url = reverse('new')
        form = {
            'brand': 'Opel',
            'model': 'Astra',
            'year': 2000,
            'seller': 2
        }
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        count = Car.objects.count()
        self.client.post(url, form)
        self.assertEqual(Car.objects.last().brand, form['brand'])
        self.assertEqual(Car.objects.filter(brand='Opel').count(), 1)
        self.assertEqual(Car.objects.count(), count + 1)
    def test_delete(self):
        url = reverse('delete_car', kwargs={
            'pk': self.car.pk
        })
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Car.objects.filter(pk=self.car.pk).count(), 0)

    def test_update(self):
        url = reverse('edit', kwargs={
            'pk': self.car.pk
        })
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        form = {
            'brand': 'Test',
            'model': 'Test',
            'year': 1,
            'seller': 2
        }
        self.client.post(url, form)
        car_brand = Car.objects.filter(brand='Test')[0].brand
        self.assertEqual(car_brand, form['brand'])
