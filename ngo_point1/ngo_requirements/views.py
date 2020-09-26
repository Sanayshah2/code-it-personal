from django.shortcuts import render

# Create your views here.
def home(request):
   # group=Group.objects.get(user=request.user)
    return render(request,'ngo_requirements/home.html')