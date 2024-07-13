from django.urls import path
# Precisa-se importar o views
from . import views

app_name = 'users'

urlpatterns = [
    # Como nao existe url esta e a pagina default
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
