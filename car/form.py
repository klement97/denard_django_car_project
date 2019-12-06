from django import forms

from .models import Cars


class Edit_Car(forms.Form):
    model = Cars
    fields = ['brand', 'model', 'year']


class Add_New_Car(forms.Form):
    brand = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    year = forms.IntegerField()
