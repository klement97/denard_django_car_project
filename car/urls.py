from django.urls import path

from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('<int:pk>/', views.CarDetails.as_view()),
    path('car_list/new/', views.new_car, name="new"),
    path('car_list/new/add/', views.AddNewCar.as_view()),
    path('car_list/delete_car/<int:pk>/', views.CarDelete.as_view()),
    path('car_list/edit/<int:pk>/', views.CarEdit.as_view()),
]
