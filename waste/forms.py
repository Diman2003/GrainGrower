from django.forms import ModelForm

from .models import Waste


class WasteForm(ModelForm):
    class Meta:
        model = Waste
        exclude = ('user',)