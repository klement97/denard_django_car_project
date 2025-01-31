from django.urls import path

from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('<int:pk>/', views.CarDetails.as_view(), name='car_details'),
    path('car_list/new/add/', views.AddNewCar.as_view(), name='new'),
    path('car_list/delete_car/<int:pk>/', views.CarDelete.as_view(), name='delete_car'),
    path('car_list/edit/<int:pk>/', views.CarEdit.as_view(), name='edit'),
]
