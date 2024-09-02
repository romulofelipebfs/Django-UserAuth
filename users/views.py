from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def homepage(request):
    return render(request, "users/index.html")


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")


    return render(request, "users/register.html", {
        'form':form
    })



def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")



    return render(request, "users/my-login.html", {
        "form":form
    })

def user_logout(request):

    auth.logout(request)
    
    return redirect("")

@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'users/dashboard.html')