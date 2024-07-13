from django.urls import path
# Precisa-se importar o views
from . import views

app_name = 'posts'

urlpatterns = [
    # Como nao existe url esta e a pagina default
    path('', views.posts_list_view, name="list"),
    path('<slug:slug>', views.post_page_view, name="page"),
]
