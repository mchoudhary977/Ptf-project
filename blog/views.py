from django.shortcuts import render, get_object_or_404
#To have detailed view of each blog using blog id (step-3) add get_object_or_404

from .models import Blog
# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

#To have detailed view of each blog using blog id (step-3)
def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/blogdetail.html',{'blog':detailblog})
