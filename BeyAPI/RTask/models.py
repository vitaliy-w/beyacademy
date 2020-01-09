from django.db import models


# Create your models here.
class rtask(models.Model):
    ua = models.CharField(max_length=200)
    ru = models.CharField(max_length=200)
    en = models.CharField(max_length=200)
    nl = models.CharField(max_length=200)
    de = models.CharField(max_length=200)

    #> ~/beyacademy/BeyAPI$ python3 manage.py migrate
    #> AttributeError: module 'django.forms.models' has no attribute 'Model'



