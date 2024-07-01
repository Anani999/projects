# forms.py

from django import forms

class CheckoutForm(forms.Form):
    amount = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
