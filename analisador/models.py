from django.db import models
import os
import shutil


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100)
    style = models.CharField(default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


class imagem(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50,default='')

class audio(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50,default='')

class video(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50,default='')

class texto(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50,default='')

class outros(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=50,default='')

class UploadImage(models.Model):
    imagem = models.FileField(upload_to='documents')
    imagem2 = models.FileField(upload_to='documents')
