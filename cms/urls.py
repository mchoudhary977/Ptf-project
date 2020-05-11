#adding for cert details sectino (step-2)
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.allcerts, name='allcerts'),
    #To have detailed view of each blog using blog id (step-1)
    path('<int:cert_id>/',views.certdetail,name='certdetail'),
]
