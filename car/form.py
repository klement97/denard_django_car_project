from django import forms


class Add_New_Car(forms.Form):
    brand = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    year = forms.IntegerField()
