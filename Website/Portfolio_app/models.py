from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1000)
    technology_used = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='projects')
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='skills')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    experience = models.IntegerField()
    designation = models.CharField(max_length=1000)
    description1 = models.TextField(max_length=1000)
    description2 = models.TextField(max_length=1000)
    get_cv = models.CharField(max_length=1000)
    download_cv = models.CharField(max_length=1000)
    git_hub = models.CharField(max_length=1000)
    linkdin = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
