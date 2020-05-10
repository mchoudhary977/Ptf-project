from django.shortcuts import render

from .models import Certificate
from we.models import WorkExp
import we.views

# Create your views here.
def home(request):
    workexp = WorkExp.objects
    certificates = Certificate.objects
    return render(request,'cms/home.html',{'certificates':certificates,'workexp':workexp})
