from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Blogs


def getblog(id):
    blog = Blogs.objects.get(id=id)
    return blog


def home(request):
    blogs = Blogs.objects.all()
    return render(request,'home.html',context={'blogs':blogs})

def blog(request,id):
    blog = getblog(id)
    if(blog):
        print(blog)
        return render(request,'blog.html',context={'blog':blog})
    
def update(request,id):
    blog = getblog(id)
    if request.method == "POST":
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        if 'image' in request.FILES:
            file = request.FILES['image']
            blog.image = file
        blog.heading = heading
        blog.body = content
        blog.save()
        return HttpResponse('response submitted !')
        
    else:
        return render(request,'update_blog.html',context={'blog':blog})

def delete(request,id):
    blog = getblog(id)
    blog.delete()
    return HttpResponse('blog is delteted ')

def create(request):
    new_blog = Blogs.objects.create(heading='',body='')
    new_blog.save()
    return redirect(f"update-blog/{new_blog.id}/")
