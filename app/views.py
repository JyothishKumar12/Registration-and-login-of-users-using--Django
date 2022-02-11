from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.forms import CreateUserform
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib.auth.decorators import login_required


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserform()
        if request.method == "POST":
            form = CreateUserform(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,user+'Registered Sucessfully')
                return redirect('login')
    return render(request,'registration.html',{'Form':form})



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
    return render(request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
