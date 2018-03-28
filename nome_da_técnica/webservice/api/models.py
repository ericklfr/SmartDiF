from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

class SomarAPI(models.Model):
    valor1 = models.IntegerField(default=0)
    valor2 = models.IntegerField(default=0)




