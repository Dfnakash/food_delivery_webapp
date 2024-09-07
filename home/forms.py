# forms.py
from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'address', 
            'city', 
            'state', 
            'postal_code', 
            'country', 
            'payment_method'
        ]
