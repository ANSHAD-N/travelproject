from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, "already have an account")
                return redirect("register")
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                print("user created")
                messages.success(request, "user created")
                return redirect('login')
        else:
            messages.warning(request, "password not matched")
            return redirect("register")
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')