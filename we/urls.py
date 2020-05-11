#adding for work details sectino (step-2)
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.allwork, name='allwork'),
    #To have detailed view of each woek experience using work id (step-1)
    path('<int:work_id>/',views.workdetail,name='workdetail'),
]
