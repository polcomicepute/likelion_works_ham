from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# from .forms import BlogUpdate

# Create your views here.
from .forms import BlogUpdate

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})
def hello(request):
    return render(request, 'hello.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))


def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def detail(request, blog_id):
    blog_datail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_datail})
    
def blog(request):
    blogs=Blog.objects
    return render(request, 'blog.html', {'blogs':blogs})


def new(request):
    return render(request, 'new.html')

def mypage(request):
    return render(request, 'mypage.html')


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})