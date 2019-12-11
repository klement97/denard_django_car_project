from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView, DetailView, UpdateView, CreateView)

from car.models import Car
from .form import EditCarForm


# display cars in a list

class CarListView(ListView):
    template_name = "car/index.html"
    model = Car
    context_object_name = "car_list"
    paginate_by = 5

# display details of idividual car

class CarDetails(DetailView):
    model = Car
    template_name = "car/car_details.html"


# render the form to add a new car

def new_car(request):
    form = EditCarForm()
    return render(request, "../templates/car/new_car.html", {'form': form})


# AddNewCar class

class AddNewCar(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/'


# Delete car class
class CarDelete(DeleteView):
    model = Car
    success_url = '/'


# editing the car
# CarEdit class is not finished
# todo: check for the outputs in the html

class CarEdit(UpdateView):
    model = Car
    form_class = EditCarForm
    template_name = 'car/edit_car.html'
    success_url = reverse_lazy('index')
