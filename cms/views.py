from django.shortcuts import render

from .models import Certificate
# Create your views here.
def home(request):
    certificates = Certificate.objects
    return render(request,'cms/home.html',{'certificates':certificates})
