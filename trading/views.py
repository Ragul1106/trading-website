from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .models import AboutContent

def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('register')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, "trading/layout/register.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "trading/layout/login.html")

def home(request):
    return render(request, "trading/layout/home.html")


def about_view(request):
    content = AboutContent.objects.first()
    # Prepare a list of row images
    row_images = [
        content.row_image_1,
        content.row_image_2,
        content.row_image_3,
        content.row_image_4,
    ] if content else []

    return render(request, 'trading/layout/about.html', {'content': content, 'row_images': row_images})

def user_logout(request):
    logout(request)
    return redirect('login')