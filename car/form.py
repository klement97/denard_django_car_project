from django import forms

from .models import Cars


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['brand', 'model', 'year']




class Add_New_Car(forms.Form):
    brand = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    year = forms.IntegerField()
