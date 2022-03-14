from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("admin_home")
            elif user.is_college:
                return redirect("home")
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'home.html')

def college_register(request):
    user_form = loginregister()
    college_form = collegeregister()
    if request.method == 'POST':

        user_form = loginregister(request.POST)
        college_form = collegeregister(request.POST)
        if user_form.is_valid() and college_form.is_valid():
            user = user_form.save(commit=False)
            user.is_college = True
            user.save()
            college = college_form.save(commit=False)
            college.user = user
            college.save()
            messages.info(request, 'college Registered Successfully')
            return redirect('loginview')
    return render(request, 'collegeregister.html', {'user_form': user_form, 'college_form': college_form})


@login_required(login_url='loginview')
def home(request):
    return render(request, 'college.html')

@login_required(login_url='loginview')
def addstudent(request):
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewstudent")
    else:
        form = studentform()
        return render(request, 'addstudent.html', {'form': form})


@login_required(login_url='loginview')
def viewstudent(request):
    data = student.objects.filter(user=request.user)
    print(data)
    return render(request, 'viewstudent.html', {'data': data})


@login_required(login_url='loginview')
def admin_home(request):
    data = college.objects.all()
    print(data)
    return render(request, 'admin_home.html', {'data': data})


def logout_view(request):
    logout(request)
    return redirect('loginview')

def main(request):
    return render(request, 'main.html')

