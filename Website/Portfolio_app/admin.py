from django.contrib import admin
from .models import Project, Skill, User


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(User)
admin.site.site_header = "Welcome"
