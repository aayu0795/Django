# Generated by Django 2.2 on 2020-02-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_app', '0002_auto_20200209_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
