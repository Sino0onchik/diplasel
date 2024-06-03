from .models import *
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Order

