from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView, DetailView, UpdateView, CreateView)

from .form import EditSellers
from .models import Seller


# display cars in a list
# view seller list
class SellerListView(LoginRequiredMixin, ListView):
    template_name = "sellers_list.html"
    model = Seller
    context_object_name = "seller_list"
    paginate_by = 5
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'


# seller details
class SellerDetails(LoginRequiredMixin, DetailView):
    model = Seller
    template_name = "seller_details.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

# add new seller
class AddSeller(LoginRequiredMixin, CreateView):
    model = Seller
    fields = '__all__'
    template_name = 'new_seller.html'
    success_url = reverse_lazy('seller_list')
    redirect_field_name = 'redirect_to'


# delete seller

class DeleteSeller(LoginRequiredMixin, DeleteView):
    model = Seller
    success_url = "/seller_list"
    template_name = 'seller_confirm_delete.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

# update seller

class EditSeller(LoginRequiredMixin, UpdateView):
    model = Seller
    form_class = EditSellers
    template_name = 'edit_seller.html'
    success_url = '/seller_list'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
