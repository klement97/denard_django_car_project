from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (ListView)

from car.models import Cars
from .form import Add_New_Car


class CarListView(ListView):
    template_name = "car/index.html"
    model = Cars
    context_object_name = "car_list"


def details(request, car_id):
    car = Cars.objects.get(id=car_id)
    context = {
        'brand': car.brand,
        'model': car.model,
        'year': car.year
    }
    return render(request, "../templates/car/car_details.html", context)



def new_car(request):
    form = Add_New_Car()
    return render(request, "../templates/car/new_car.html", {'form': form})


def add_car(request):
    if request.method == "POST":
        form = Add_New_Car(request.POST)
        if form.is_valid():
            brand = form.cleaned_data["brand"]
            model = form.cleaned_data["model"]
            year = form.cleaned_data["year"]
            Cars.objects.create(
                brand=brand,
                model=model,
                year=year
            )
            return HttpResponseRedirect("/")
    elif request.method == 'GET':
        return HttpResponseRedirect("new/")


def get_car(request, car_id):
    car = Cars.objects.get(id=car_id)
    context = {
        'brand': car.brand,
        'model': car.model,
        'year': car.year
    }
    return render(request, "../templates/car/edit_car.html", context)


def edit_car(request, car_id):
    car = Cars.objects.get(id=car_id)
    if request.method == "POST":
        car.brand = request.POST.get("car_brand")
        car.model = request.POST.get("car_model")
        car.year = request.POST.get("car_year")
        car.save()
    return HttpResponseRedirect('/')


def delete_car(request, car_id):
    Cars.objects.get(id=car_id).delete()
    return HttpResponseRedirect("/")
