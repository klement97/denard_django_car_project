from django import forms

from .models import Sellers


class EditSellers(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['name', 'country', 'city', 'address']
