from django.shortcuts import render, get_object_or_404

from .models import Certificate
from we.models import WorkExp
import we.views

# Create your views here.
def home(request):
    workexp = WorkExp.objects
    certificates = Certificate.objects
    return render(request,'cms/home.html',{'certificates':certificates,'workexp':workexp})

def allcerts(request):
    certs = Certificate.objects
    return render(request,'cms/allcerts.html',{'certs':certs})

#To have detailed view of each blog using blog id (step-3)
def certdetail(request, cert_id):
    certdetail = get_object_or_404(Certificate, pk=cert_id)
    return render(request,'cms/certdetail.html',{'certdetail':certdetail})
