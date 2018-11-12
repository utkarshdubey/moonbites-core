from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post

def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})

def detail(request, pk):
  posts = get_object_or_404(Post, pk=pk)
  return render(request, 'detail.html', {'posts': posts})

def add(request):
  if request.POST['password'] == "utkarsh1!":
    new_post = Post(title=request.POST['title'], author_name=request.POST['author'], author_website=request.POST['author_website'], short_description=request.POST['description'], content=request.POST['content'], genre=request.POST['genre'])
    new_post.save()  
    return HttpResponseRedirect('/')
def post(request):
  return render(request, 'post.html')