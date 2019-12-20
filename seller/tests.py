# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from car.models import Car
from seller.form import EditSellers
from seller.models import Seller


class SellerTest(TestCase):
    """
         Test class for Seller Views.
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

    def test_seller_list_view(self):
        """
             Ensure we can list all the sellers.
             Ensure that the pagination works.
        """
        url = reverse('seller_list')
        response = self.client.get(url)

        # Confirm we get a response
        self.assertEquals(response.status_code, 200)

        # Confirm that the pagination by 5 works
        context_data = response.context_data
        list = len(context_data['page_obj'].object_list)
        self.assertLessEqual(list, 5)

        # Confirm we get the right objects rendered
        seller = Seller.objects.all()
        object_list = context_data['object_list']
        self.assertEquals(seller.query, object_list.query)

    def test_seller_create(self):
        """
            Ensure we get the right model form to create the seller.
            Ensure we can create a seller with form data given below.
            Ensure we get riderected after the car creation to the right url
        """
        url = reverse('add_seller')
        form = {
            'name': 'TestName',
            'country': 'some land',
            'city': 'some city',
            'address': 'some address'
        }

        response = self.client.get(url)
        # Confirm we get a response back
        self.assertEquals(response.status_code, 200)

        # Confirm that the view gives all the fields from the model to fill in
        view_fields = response.context_data['view'].fields
        self.assertEquals(view_fields, '__all__')

        # Confirm that the form is rendered from the Car model
        seller_model_form = response.context_data['form'].Meta.model
        self.assertEquals(seller_model_form, Seller)

        # Confirm that the new object is created
        count = Seller.objects.count()
        self.client.post(url, form)
        self.assertEqual(Seller.objects.last().name, form['name'])
        self.assertEqual(Seller.objects.filter(name='TestName').count(), 1)
        self.assertEqual(Seller.objects.count(), count + 1)

        # Confirm that the view renders in  the right template
        success_url = response.context_data['view'].success_url
        self.assertTemplateUsed(response, 'new_seller.html')
        self.assertEquals(success_url, '/seller_list/')

    def test_seller_delete(self):
        """
            Ensure that the seller is deleted
            Ensure that the view used is the delete_seller view
            Ensure we get riderected after the car creation to the right url

        """
        url = reverse('delete_seller', kwargs={
            'pk': self.seller.pk
        })
        response = self.client.delete(url)
        view_name = response.resolver_match.view_name
        self.assertEquals(view_name, 'delete_seller')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Seller.objects.filter(pk=self.seller.pk).count(), 0)

        self.assertEquals(response.url, '/seller_list/')

    def test_update(self):
        """
            Ensure that the car is updated
            Ensure we get the right form to update the car
            Ensure we get riderected after the car creation to the right url
        """
        url = reverse('update_seller', kwargs={
            'pk': self.seller.pk
        })

        response = self.client.get(url)

        # Confirm that we get data
        self.assertEquals(response.status_code, 200)

        # Confirm we get back the right form
        form = response.context_data['form']
        original_form = EditSellers()
        self.assertEqual(len(form.fields), len(original_form.fields))
        self.assertEquals(form.Meta, original_form.Meta)
        self.assertEquals(form.base_fields, original_form.base_fields)

        self.assertIsInstance(form, EditSellers)

        seller1 = response.context_data['object']
        form = {
            'name': 'TestName',
            'country': 'some land',
            'city': 'some city',
            'address': 'some address'
        }
        self.client.post(url, form)

        # Confirm that the object is updated
        response2 = self.client.get(url)
        updated_seller = response2.context_data['object']
        self.assertIsNot(seller1, updated_seller)

        # Confirm that the brand of the car si updated
        seller_name = Seller.objects.filter(name='TestName')[0].name
        self.assertEqual(seller_name, form['name'])

        # Confirm that the success url is right
        success_url = response.context_data['view'].success_url
        self.assertEquals(success_url, '/seller_list')
