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
    categories=get_all_help_categories()
    requirements = Requirement.objects.all()
    context={
        'requirements':requirements,
        'categories':categories,
    }


    return render(request,'ngo_requirements/home.html',context)

@is_logged
def register(request):
   if request.method=='POST':
      form=UserForm(request.POST)
      if form.is_valid():
            form.save()
            group = request.POST.get('group')
            group1 = Group.objects.get(name = group)
            user = form.save(commit=False)
            user.groups.add(group1)
            user.save()
            if group == 'ngo':
                ngo = Ngo(user=user)
                ngo.save()
            else:
                donor = Donor(user=user)
                donor.save()

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
   return redirect('home')


@login_required
@donor_required
def requirement_fulfillment(request,rid):
    requirement=Requirement.objects.get(id=rid)
    print(requirement)
    if request.method == 'POST':
        donor=Donor.objects.get(user=request.user)
        if requirement.amount:
            amount=request.POST.get('amount')
            print(amount)
            requirement.requirement_fulfilled+=int(amount)
        else :
            quantity=request.POST.get('quantity')
            requirement.requirement_fulfilled+=int(quantity)
        requirement.fulfilled_by.add(donor)
        requirement.save()
        return redirect('home')
    else:
        return render(request,"ngo_requirements/requirement-fulfillment.html",{'r':requirement})
        
    
    
    print(requirement.amount)
    return render(request,"ngo_requirements/requirement-fulfillment.html",{'r':requirement})
        







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

            if category == 'Financial':
                amount=request.POST.get('amount')
                instance.amount=amount
            else:
                quantity=request.POST.get('quantity')
                instance.quantity=quantity

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
    ngo=Ngo.objects.get(user=request.user)
    requirements=Requirement.objects.filter(ngo=ngo)
    context={
        'requirements':requirements,
    }

    return render(request,'ngo_requirements/ngo_dashboard.html',context)

def get_all_help_categories():
    categories = Help_category.objects.all()
    return categories

def ngoRequirementView(request,rid):
    requirement=Requirement.objects.get(id=rid)
    context={
        'requirement':requirement,
    }
    return render(request,'ngo_requirements/ngo_requirement_view.html',context)

def donorRequirementView(request,rid):
    requirement=Requirement.objects.get(id=rid)
    context={
        'requirement':requirement,
    }
    return render(request,'ngo_requirements/donor_requirement_view.html',context)