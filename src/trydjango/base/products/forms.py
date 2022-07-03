from django import forms
from .models import Product



class Productform(forms.ModelForm):
    models = Product
    fields = ['__all__']
