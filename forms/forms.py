from django import forms


class tee_shirtForm(forms.Form):
    taille = forms.NumberInput()
    poids = forms.NumberInput()