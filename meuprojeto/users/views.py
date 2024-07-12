from django.shortcuts import render
# para o slug
# verificador se esta tudo certo
from django.http import HttpResponse

# Create your views here.


def register_page(request):
    return render(request, 'users/register_page.html')