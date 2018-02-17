from django import forms


class AdressForm(forms.Form):
    adress_verge = forms.CharField(label="adress:", max_length=100)