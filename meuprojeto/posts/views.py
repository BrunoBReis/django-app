from django.shortcuts import render
from .models import Post
# para o slug
# verificador se esta tudo certo
#from django.http import HttpResponse

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
