from django import forms
from . import models

class CityModelForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields= ['name']