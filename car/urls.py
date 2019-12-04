from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_car/', views.add_new_car, name='new_car'),
]
