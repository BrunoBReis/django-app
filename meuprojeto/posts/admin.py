from django.contrib import admin
from .models import Post

# Register your models here.
# para utilizar as informacoes dos apps
# precisa-se atualizar aqui

admin.site.register(Post)