from django import forms

from .models import Seller


class EditSellers(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'country', 'city', 'address']
