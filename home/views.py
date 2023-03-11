from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Post
from .forms import PostForm

# def home(request):
#     return render(request, 'home/index.html')

# def post(request, pk):
#     return render(request, 'home/index.html')

# CRUD VIEWS
@staff_member_required
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        return redirect('home:index')
    else:
        context = {'form': form}
        return render(request, 'home/create_post.html', context)
    

@staff_member_required 
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
        return redirect('home:index')
    else:
        context = {'form': form,
                   'post': post}
        return render(request, 'home/update_post.html', context)
    


