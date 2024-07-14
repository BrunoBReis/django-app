from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# para o slug
# verificador se esta tudo certo
# from django.http import HttpResponse
from . import forms
# Create your views here.


def posts_list_view(request):
    """ Mostra todos os posts """
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page_view(request, slug):
    """ Mostra a pagina do post """
    # verificaodr se esta tudo certo
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})


@login_required(login_url="/users/login/")
def post_new_view(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})
