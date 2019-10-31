from django import forms


class StudentLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login:",
        max_length=25,
        widget=forms.TextInput()
    )
class UczelniaForm(forms.Form):
    login2 = forms.CharField(
        label="Twoja uczelnia:",
        max_length=30,
        widget=forms.TextInput()
    )
