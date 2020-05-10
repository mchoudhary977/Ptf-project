
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    #To have detailed view of each blog using blog id (step-1)
    path('<int:blog_id>/',views.detail,name='detail'),
]
