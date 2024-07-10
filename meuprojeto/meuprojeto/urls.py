"""
URL configuration for meuprojeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Precisa-se importar o views
from . import views
# importando o static
from django.conf.urls.static import static
# importando as configuracoes
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # Como nao existe url esta e a pagina default
    path('', views.homepage),
    path('about/', views.about),
    # Veja dentro do app posts a url
    path('posts/', include('posts.urls')),
    # users page
    path('users/', include('users.urls')),
]

# aonde encontrar as imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
