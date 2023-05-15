from django import forms

from .models import CustomUser, ShippingAddress


class CustomerForm(forms.ModelForm):
    pass


class ShippingAddressForm(forms.ModelForm):
    pass
