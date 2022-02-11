from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from.forms import *
# Create your views here.


def registration(request):
    form = CreateUserform()
    if request.method == "POST":
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'registration.html',{'Form':form})



def login(request):
    return render(request,'login.html')