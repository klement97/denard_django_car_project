from django.urls import path

from . import views

urlpatterns = [
    path('seller_list/', views.SellerListView.as_view(), name='seller_list'),
    path('seller/<int:pk>/', views.SellerDetails.as_view(), name="seller_details"),
    path('seller_list/add_seller/', views.AddSeller.as_view(), name='add_seller'),
    path('delete_seller/<int:pk>', views.DeleteSeller.as_view(), name="delete_seller"),
    path('edit_seller/<int:pk>/', views.EditSeller.as_view(), name="update_seller"),

]
