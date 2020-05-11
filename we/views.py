from django.shortcuts import render, get_object_or_404
#To have detailed view of each work experience using work id (step-3) add get_object_or_404

from .models import WorkExp
# Create your views here.

def allwork(request):
    works = WorkExp.objects
    return render(request,'we/allwork.html',{'works':works})

#To have detailed view of each work experience using work id (step-3)
def workdetail(request, work_id):
    workdetail = get_object_or_404(WorkExp, pk=work_id)
    return render(request,'we/workdetail.html',{'work':workdetail})
