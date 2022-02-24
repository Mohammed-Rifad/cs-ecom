from django.shortcuts import render

# Create your views here.

def reseller_home(request):
    return render(request,'home.html')