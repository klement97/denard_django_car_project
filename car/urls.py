from django.urls import path

from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='index.html'),
    path('<int:car_id>/', views.details),
    path('new/', views.new_car, name="new"),
    path('new/add/', views.add_car),
    path('delete_car/<int:car_id>/', views.delete_car),
    path('edit/<int:car_id>/', views.get_car),
    path('edit/<int:car_id>/new/', views.edit_car),
]
