from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

def homepage(r):
    return render(r,"index.html")


def applyForAdmission(r):

    form = StudentForm(r.POST  or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(r,"apply.html",{"form":form})

def login(r):

    LoginForm = AuthenticationForm(r.POST or None)
    
    return render(r,"login.html",{"form":LoginForm})

