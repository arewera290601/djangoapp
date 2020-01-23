from django import forms
from studenci.models import Miasto

class StudentLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login:",
        max_length=25,
        widget=forms.TextInput()
    )
class UczelniaForm(forms.Form):
     nazwa = forms.CharField(
        label="Twoja uczelnia:",
        max_length=30,
        widget=forms.TextInput()
     )

class MiastoForm(forms.Form):
    nazwa = forms.CharField(
        label="Nazwa miasta",
        max_length=30,
        widget=forms.TextInput()
    )
    kod = forms.CharField(
        label="Kod pocztowy",
        max_length=6,
        widget=forms.TextInput()
    )

class MiastoModelForm(forms.ModelForm):
    class Meta:
        model = Miasto
        fields = ('nazwa', 'kod')
