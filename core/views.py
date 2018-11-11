from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})

def detail(request, pk):
  posts = get_object_or_404(Post, pk=pk)
  return render(request, 'detail.html', {'posts': posts})