from django.forms import ModelForm
from pizza.models import Skladnik

class SkladnikForm(ModelForm):
    class Meta:
        model = Skladnik
        fields = ('nazwa', 'jarski', 'cena', 'pizza')
