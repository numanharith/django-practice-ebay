from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def views_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        country = request.POST['country']
        city = request.POST['city']
        username = request.POST['username']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Password is not a match.")
            return render(request, 'accounts/register.html')

        # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
        try:
            user = User.objects.create_user(
                username,
                email,
                password,
            )
            user.save()
        except IntegrityError:
            messages.error(request, "Username or email is taken")
            return render(request, "accounts/register.html")

        login(request, user)

        return redirect("products:products_index")

    form = UserCreationForm()
    return render(request, 'accounts/register.html', { 'form': form })

def views_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("products:products_index")
        else:
            messages.error(request, "Username or password is incorrect")
            return render(request, "accounts/login.html")

    return render(request, 'accounts/login.html')

def views_logout(request):
    logout(request)
    return redirect('accounts:login')