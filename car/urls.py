from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_car, name="new"),
    path('new/add/', views.add_car),
    path('delete_car/<int:car_id>/', views.delete_car),
]
