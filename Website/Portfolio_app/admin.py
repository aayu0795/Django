from django.contrib import admin
from .models import Project


admin.site.register(Project)
admin.site.site_header = "Welcome"
