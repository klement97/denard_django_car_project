from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView, DetailView, UpdateView, CreateView)

from car.models import Cars
from .form import EditCarForm, Add_New_Car


# display cars in a list

class CarListView(ListView):
    template_name = "car/index.html"
    model = Cars
    context_object_name = "car_list"


# display details of idividual car

class CarDetails(DetailView):
    model = Cars
    template_name = "car/car_details.html"
    pk_url_kwarg = 'car_id'


# render the form to add a new car

def new_car(request):
    form = Add_New_Car()
    return render(request, "../templates/car/new_car.html", {'form': form})


# AddNewCar class

class AddNewCar(CreateView):
    model = Cars
    fields = ['model', 'brand', 'year']
    success_url = '/'


# Delete car class
class CarDelete(DeleteView):
    model = Cars
    pk_url_kwarg = 'car_id'
    success_url = '/'


# editing the car
# CarEdit class is not finished

class CarEdit(UpdateView):
    model = Cars
    form_class = EditCarForm
    template_name = 'car/edit_car.html'
    success_url = reverse_lazy('index')
