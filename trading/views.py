from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .models import AboutContent, SiteAsset


def get_bull_image():
    return SiteAsset.objects.filter(key="bull").first()

def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('register')

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    context = {"bull": get_bull_image()}
    return render(request, "trading/layout/login.html", context)

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        user = User.objects.create_user(
            username=email, email=email, password=password, first_name=name
        )
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    context = {"bull": get_bull_image()}
    return render(request, "trading/layout/register.html", context)

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, "trading/layout/home.html")


def about_view(request):
    content = AboutContent.objects.first()
    why_items = [
        {"title": "Research & Recommended Stock", "icon": "images/ar4.png"},
        {"title": "Join Our Community of 5 Million + Happy Inversters", "icon": "images/ar3.png"},
        {"title": "Invest in All-in-one Platform", "icon": "images/ar2.png"},
        {"title": "Get personalized service at 160+ branches in India", "icon": "images/ar1.png"},
    ]
    return render(request, 'trading/layout/about.html', {
        'content': content,
        'why_items': why_items
    }) 
    
