from django import forms
from rest_framework import serializers




class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.CharField(default='python')
    style = serializers.CharField(default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class SomarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    valor1 = serializers.IntegerField()
    valor2 = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Somar.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.valor1 = validated_data.get('valor1', instance.valor1)
        instance.valor2 = validated_data.get('valor2', instance.valor2)
        instance.save()
        return instance

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



