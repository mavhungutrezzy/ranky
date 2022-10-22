from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render


def signin(request):
    if request.method != "POST":
        return render(request, "signin.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is None:
        return render(
            request, "login.html", {"error": "Username or password is incorrect."}
        )
    login(request, user)
    return redirect("home")


def register(request):
    if request.method != "POST":
        return render(request, "register.html")
    first_name = request.POST["first-name"]
    last_name = request.POST["last-name"]
    username = request.POST["email"]
    password = request.POST["password"]
    confirmation = request.POST["confirmation"]
    if password != confirmation:
        return render(request, "register.html", {"error": "Passwords must match."})
    try:
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )
    except IntegrityError:
        return render(
            request, "register.html", {"error": "Email address is already in use."}
        )
    login(request, user)
    return redirect("home")


@login_required
def logout(request):
    logout(request)
    return redirect("home")
