from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login as LoginFun,logout as LogoutFun
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(r):
    return render(r,"index.html")


def applyForAdmission(r):

    form = StudentForm(r.POST  or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
        
        else:
            return redirect(homepage)
    return render(r,"apply.html",{"form":form})

def login(r):

    LoginForm = AuthenticationForm( r, data=r.POST or None)
    

    if r.method == "POST":
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                print(user)
                LoginFun(r,user)
                return redirect(homepage)
                
            else:
                return redirect(login)

            return LoginForm
    return render(r,"login.html",{"form":LoginForm})


def logout(r):
    LogoutFun(r)
    return render(r,"login.html")

@login_required()
def manageStudents(r):
    data = {}
    data['students'] = Student.objects.all()
    return render(r,"admin/manageStudents.html",data)


@login_required()
def deleteStudent(r,id):
    std = Student.objects.get(pk=id)
    std.delete()
    return redirect(manageStudents)

@login_required
def editStudent(r,id):
    std = Student.objects.get(pk=id)
    form = StudentForm(r.POST or None,r.FILES or None,instance=std)

    if r.method == "POST":
        form.save()
        return redirect(manageStudents)
    return render(r,"admin/editStudent.html",{"form":form})

def viewStudent(r,id):
    student = Student.objects.get(pk=id)
    return render(r,"admin/viewStudent.html",{"student":student})
