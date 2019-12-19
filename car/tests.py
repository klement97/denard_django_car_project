from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from car.form import EditCarForm
from car.models import Car
from seller.models import Seller


class CarTest(TestCase):
    """
        Test class for Car Views.
    """
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
        """
             Ensure we can list all the cars.
             Ensure that the pagination works.
        """
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        context_data = response.context_data
        list = len(context_data['page_obj'].object_list)
        self.assertLessEqual(list, 5)

        # comparing the query sets
        cars = Car.objects.all()
        object_list = context_data['object_list']
        self.assertEquals(cars.query, object_list.query)
        self.assertTemplateUsed(response, 'car/car_list.html')
    def test_car_create(self):
        """
            Ensure we get the right model form to create the car.
            Ensure we can create a car with form data given below.
            Ensure we get riderected after the car creation to the right url
        """
        url = reverse('new')
        form = {
            'brand': 'Opel',
            'model': 'Astra',
            'year': 2000,
            'seller': 2
        }
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        view_fields = response.context_data['view'].fields
        self.assertEquals(view_fields, '__all__')

        car_model_form = response.context_data['form'].Meta.model
        self.assertEquals(car_model_form, Car)

        count = Car.objects.count()
        self.client.post(url, form)
        self.assertEqual(Car.objects.last().brand, form['brand'])
        self.assertEqual(Car.objects.filter(brand='Opel').count(), 1)
        self.assertEqual(Car.objects.count(), count + 1)

        success_url = response.context_data['view'].success_url
        self.assertEquals(success_url, '/car_list/')
        self.assertTemplateUsed(response, 'car/car_list.html')

    def test_delete(self):
        """
            Ensure that the car is deleted
            Ensure that the view used is the delete_car view
            Ensure we get riderected after the car creation to the right url

        """
        url = reverse('delete_car', kwargs={
            'pk': self.car.pk
        })
        response = self.client.delete(url)
        view_name = response.resolver_match.view_name
        self.assertEquals(view_name, 'delete_car')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Car.objects.filter(pk=self.car.pk).count(), 0)

        self.assertEquals(response.url, '/car_list/')


    def test_update(self):
        """
            Ensure that the car is updated
            Ensure we get the right form to update the car
            Ensure we get riderected after the car creation to the right url
        """
        url = reverse('edit', kwargs={
            'pk': self.car.pk
        })
        response = self.client.get(url)

        # confirm that we get data back
        self.assertEquals(response.status_code, 200)

        # confirm we get back the right form
        form = response.context_data['form']
        original_form = EditCarForm()
        self.assertEqual(len(form.fields), len(original_form.fields))
        self.assertEquals(form.Meta, original_form.Meta)
        self.assertEquals(form.base_fields, original_form.base_fields)

        form = {
            'brand': 'Test',
            'model': 'Test',
            'year': 1,
            'seller': 2
        }
        self.client.post(url, form)
        # confirm that the brand of the car si updated
        car_brand = Car.objects.filter(brand='Test')[0].brand
        self.assertEqual(car_brand, form['brand'])
        # confirm that the success url is right
        success_url = response.context_data['view'].success_url
        self.assertEquals(success_url, '/car_list/')
