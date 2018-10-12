from django import forms



class ImagemForm(forms.Form):
    resultado = forms.ImageField(widget=forms.FileInput(attrs={'id':'file','onchange':'loadImage();'}))

class FacesForm(forms.Form):
    x_min = forms.CharField();
