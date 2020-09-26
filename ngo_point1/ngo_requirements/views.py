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
            ngo = Ngo(user=user)
            ngo.save()

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
                  return redirect('donorDashboard')
                else:
                  login(request, user)
                  return redirect('ngoDashboard')
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
def donorDashboard(request):
   return render(request,"ngo_requirements/donordashboard.html")





def addRequirement(request):
    categories= get_all_help_categories()
    if request.method=='POST':
        ngo=Ngo.objects.get(user=request.user)
        print(ngo)
        category=request.POST.get('category')
        print(category)
        category1=Help_category.objects.get(help_category = category)
        
        form=AddRequirementForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)

            #print(category1)
            instance.category=category1

            instance.ngo=ngo
            instance.save()
            return redirect('addRequirement')
        else:
            messages.info(request, f"Error occured.")
    else:
        form=AddRequirementForm()
    return render(request,'ngo_requirements/addRequirement.html',{'form':form,'categories':categories})



@login_required
@ngo_required

def ngoDashboard(request):
    return render(request,'ngo_requirements/ngo_dashboard.html')

def get_all_help_categories():
    categories = Help_category.objects.all()
    return categories
