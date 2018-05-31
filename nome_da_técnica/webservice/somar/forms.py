from django import forms
from somar.models import Somar

class Somar(forms.ModelForm):

    class Meta:
        model = Somar
        fields = ['valor1', 'valor2']

class ImagemForm(forms.Form):
    resultado = forms.FileField(widget=forms.FileInput(attrs={'id':'file','onchange':'loadImage();'}))
