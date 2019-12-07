from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='index'),
    path('<int:car_id>/', views.CarDetails.as_view()),
    path('new/', views.new_car, name="new"),
    path('new/add/', views.AddNewCar.as_view()),
    path('delete_car/<int:car_id>/', views.CarDelete.as_view()),
    path('edit/<int:pk>/', views.CarEdit.as_view()),
    path('edit/<int:car_id>/new/', views.CarEdit.as_view()),
]
