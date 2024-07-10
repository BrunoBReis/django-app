from django.urls import path
# Precisa-se importar o views
from . import views

app_name = 'users'

urlpatterns = [
    # Como nao existe url esta e a pagina default
    path('register/', views.register_page, name="register"),
]
