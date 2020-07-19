from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# from .forms import BlogUpdate
from django.core.paginator import Paginator
# Create your views here.
from .forms import BlogUpdate
from faker import Faker
myfake = Faker()



def blog(request):#page를 views에서 한번 걸러줘서 진행
    blogs = Blog.objects
    blog_list=Blog.objects.all() #blog를 가져오는 방식이 query set
    paginator = Paginator(blog_list, 10) #그걸 1개씩 잘라서 페이지를 만들어줘
    page =request.GET.get('page') #실제로 페이지에 들어가는 내용을 가져와줘
    articles = paginator.get_page(page) # 그걸 뿌릴 수 있게 바꿔줘 (객체로)

    return render(request,'blog.html', {'blogs':blogs, 'articles':articles})

 
        
def hello(request):
    return render(request, 'hello.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def fake(request):
    for i in range(10):
        blog = Blog()
        blog.title =myfake.sentence()
        blog.body = myfake.text()
        blog.pub_date = timezone.datetime.now()
        blog.save()
    return redirect('/')
    # blogs = Blog.objects
    # blog_list=Blog.objects.all() #blog를 가져오는 방식이 query set
    # paginator = Paginator(blog_list, 10) #그걸 1개씩 잘라서 페이지를 만들어줘
    # page =request.GET.get('page') #실제로 페이지에 들어가는 내용을 가져와줘
    # articles = paginator.get_page(page) # 그걸 뿌릴 수 있게 바꿔줘 (객체로)

    # return render(request,'blog.html', {'blogs':blogs, 'articles':articles})

def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def detail(request, blog_id):
    blog_datail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_datail})
    


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