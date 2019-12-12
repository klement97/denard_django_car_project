from django.shortcuts import render
from django.views.generic import (ListView, DeleteView, DetailView, UpdateView, CreateView)

from .form import EditSellers
from .models import Seller


# display cars in a list
# view seller list
class SellerListView(ListView):
    template_name = "sellers_list.html"
    model = Seller
    context_object_name = "seller_list"
    paginate_by = 5


# seller details
class SellerDetails(DetailView):
    model = Seller
    template_name = "seller_details.html"


# add new seller

def new_seller(request):
    form = EditSellers()
    return render(request, "../templates/new_seller.html", {'form': form})


class AddSeller(CreateView):
    model = Seller
    fields = ['name', 'country', 'city', 'address']
    success_url = "/seller_list"


# delete seller

class DeleteSeller(DeleteView):
    model = Seller
    success_url = "/seller_list"
    template_name = 'seller_confirm_delete.html'


# update seller

class EditSeller(UpdateView):
    model = Seller
    form_class = EditSellers
    template_name = 'edit_seller.html'
    success_url = '/seller_list'
