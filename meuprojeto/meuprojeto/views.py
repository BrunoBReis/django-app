# from django.http import HttpResponse
# faz uma busca em settings para saber onde estao os templates
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Pagina do sobre")
    return render(request, 'about.html')
