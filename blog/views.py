from django.shortcuts import redirect, render
from django.contrib import messages
from blog.forms import PostForm
from .models import Post

# Create your views here.
def create_post(requset):
    if requset.method == "GET":
        context = {'form': PostForm()}
        return render(requset,'blog/post_form.html',context)
    elif requset.method == "POST":
        form = PostForm(requset.POST)
        if form.is_valid():
            form.save()
            messages.success(requset, "The post has been created succusfully!!!")
            return redirect('posts')
        else:
            messages.error(requset, "Please correct the following errors:")
            return render(requset, 'blog/post_form.html',{'form':form})
        
def home(request):
    posts = Post.objects.all()
    content = {'posts':posts}
    return render(request, 'blog/home.html',content)

def about(request):
    return render(request, 'blog/about.html')