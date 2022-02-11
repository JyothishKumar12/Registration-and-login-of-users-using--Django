from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.forms import CreateUserform
from django.contrib import messages
# Create your views here.


def registration(request):
    form = CreateUserform()
    if request.method == "POST":
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,user+'Registered Sucessfully')
            return redirect('login')
    return render(request,'registration.html',{'Form':form})



def login(request):
    return render(request,'login.html')