from django.db import models

# Create your models here.

class Post(models.Model):
    """ Postagem de informacoes em um determiando site """
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        """ Na chamada do metodo o title aparece """
        return self.title