from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render

from car.models import Cars
from .form import Add_New_Car


def index(request):
    car_list = Cars.objects.order_by('brand')
    return render(request, "../templates/car/index", {"car_list": car_list, })


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
            created_car = Cars.objects.create(
                brand=brand,
                model=model,
                year=year
            )
            return HttpResponseRedirect("/")
    elif request.method == 'GET':
        return HttpResponseRedirect("new/")


def delete_car(request, car_id):
    Cars.objects.get(id=car_id).delete()
    return HttpResponseRedirect("/")
