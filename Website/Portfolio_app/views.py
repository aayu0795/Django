from django.shortcuts import render
from .models import Project, Skill, User

# Create your views here.


def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    user = User.objects.all()
    return render(request, 'index.html', {'projects': projects, 'skills': skills, 'my': user[0]})

