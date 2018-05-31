from django import forms



cores = (
    ('vermelho', 'Vermelho'),
    ('verde', 'Verde'),
    ('amarelo', 'Amarelo'),
    ('azul', 'Azul'),
)



class Submit(forms.Form):
    url = forms.URLField()


class ImagemForm(forms.Form):
    resultado = forms.FileField(widget=forms.FileInput(attrs={'id':'file','onchange':'loadImage();'}))


class ImagemTForm(forms.Form):
    resultado = forms.FileField(required=True)
    resultado2 = forms.FileField(required=True)

class ImagemCForm(forms.Form):
    resultado = forms.FileField(required=True)
    resultado2 = forms.ChoiceField(choices=cores)


class GrauForm(forms.Form):
    resultado = forms.IntegerField()



