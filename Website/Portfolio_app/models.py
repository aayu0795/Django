from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=1000)
    technology_used = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='pics')
    link = models.CharField(max_length=1000)
