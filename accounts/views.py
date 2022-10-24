from django.contrib.auth import authenticate, login, logout as signout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib import messages


def signin(request):
    if request.method != "POST":
        return render(request, "signin.html")
    username = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, "Invalid username and/or password"),
        return render(request, "signin.html")
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
        messages.error(request, "User already exists"),

        return render(request, "register.html")
    login(request, user)
    return redirect("home")


@login_required
def logout(request):
    signout(request)
    return redirect("home")
