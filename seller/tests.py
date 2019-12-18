# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from car.models import Car
from seller.models import Seller


class SellerTest(TestCase):
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

    def test_seller_list_view(self):
        url = reverse('seller_list')
        response = self.client.get(url)
        self.assertEquals(len(self.databases), 1)
        self.assertEquals(response.status_code, 200)

    def test_seller_create(self):
        url = reverse('add_seller')
        form = {
            'name': 'TestName',
            'country': 'some land',
            'city': 'some city',
            'address': 'some address'
        }
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.client.post(url, form)
        Seller.objects.last().refresh_from_db()
        self.assertEqual(Seller.objects.last().name, form['name'])

    def test_seller_delete(self):
        url = reverse('delete_seller', kwargs={
            'pk': self.seller.pk
        })
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Seller.objects.filter(pk=self.seller.pk).count(), 0)

    def test_update(self):
        url = reverse('update_seller', kwargs={
            'pk': self.seller.pk
        })
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        form = {
            'name': 'TestName',
            'country': 'some land',
            'city': 'some city',
            'address': 'some address'
        }
        self.client.post(url, form)
        seller_name = Seller.objects.filter(name='TestName')[0].name
        self.assertEqual(seller_name, form['name'])
