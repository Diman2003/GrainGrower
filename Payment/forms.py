from django import forms
from Payment.models import BillingAddress

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address','zipcode','city','country']
