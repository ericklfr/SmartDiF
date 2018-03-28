from django.db import models
from django.utils import timezone
import os
import shutil





class Somar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    valor1 = models.IntegerField(default=0)
    valor2 = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)



class UploadImage(models.Model):
    imagem = models.FileField(upload_to='documents')
    imagem2 = models.FileField(upload_to='documents')


class imagem(models.Model):
    titulo = models.CharField(max_length=50)


class audio(models.Model):
    titulo = models.CharField(max_length=50)


class video(models.Model):
    titulo = models.CharField(max_length=50)


class texto(models.Model):
    titulo = models.CharField(max_length=50)


class outros(models.Model):
    titulo = models.CharField(max_length=50)


