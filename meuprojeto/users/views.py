from django.shortcuts import render, redirect
# para o slug
# verificador se esta tudo certo
from django.http import HttpResponse
# Creation form
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:    
        form = UserCreationForm()
    return render(request, 'users/register_page.html', {"form": form})
