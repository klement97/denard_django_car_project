from django.shortcuts import render

from car.models import Cars
from .form import Add_New_Car


def index(request):
    car_list = Cars.objects.order_by('brand')[:5]
    context = {
        "car_list": car_list,
    }
    return render(request, "../templates/car/index", context)


def add_new_car(request):
    form = Add_New_Car()
    return render(request, "../templates/car/index", {'form': form})
