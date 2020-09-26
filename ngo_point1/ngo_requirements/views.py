from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.utils import timezone
from .decorators import *


# Create your views here.
def home(request):
   
    requirements = Requirement.objects.all()
    context={
        'requirements':requirements,
    }


    return render(request,'ngo_requirements/home.html',context)

@is_logged
def register(request):
   if request.method=='POST':
      form=UserForm(request.POST)
      if form.is_valid():
            form.save()
            group = request.POST.get('group')
            group = Group.objects.get(name = group)
            user = form.save(commit=False)
            user.groups.add(group)
            user.save()
            return redirect('login')    
   else:
      form=UserForm()
   return render(request,'ngo_requirements/register.html',{'form':form})

@is_logged
def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            if user is not None:
                group=Group.objects.get(user=user)
                g=group.name
                if g == 'donor':
                  login(request, user)
                  return redirect('donordashboard', username = user.username)
                else:
                  login(request, user)
                  return redirect('ngodashboard', username = user.username)
            elif user is None:
                messages.info(request, f'Invalid Credentials.')
    else:
        form= LoginForm()
    return render(request,"ngo_requirements/login.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@donor_required
def donordashboard(request, username):
   return render(request,"ngo_requirements/donordashboard.html")


@login_required
@ngo_required
def ngodashboard(request, username):
   return render(request,"ngo_requirements/ngodashboard.html")