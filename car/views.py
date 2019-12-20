from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView, DetailView, UpdateView, CreateView)

from car.models import Car
from .form import EditCarForm


# display cars in a list

class CarListView(LoginRequiredMixin, ListView):
    template_name = "car/car_list.html"
    model = Car
    context_object_name = "car_list"
    paginate_by = 5
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect'


# display details of idividual car

class CarDetails(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "car/car_details.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect'

# AddNewCar class
class AddNewCar(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    template_name = 'car/new_car.html'
    success_url = reverse_lazy('car_list')
    redirect_field_name = 'redirect_to'


# Delete car class
class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'car/car_confirm_delete.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'


# editing the car

class CarEdit(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = EditCarForm
    template_name = 'car/edit_car.html'
    success_url = reverse_lazy('car_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'


def redirect(request):
    return HttpResponseRedirect('/accounts/login/')
