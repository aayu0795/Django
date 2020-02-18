from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def signup(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            user = User.objects.create_user(username=username, password=password,
                                            email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('/')

        else:
            print("Password not matching")

    return render(request, 'signup.html')