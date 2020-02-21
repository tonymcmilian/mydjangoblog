from django.db import models

# Create your models here.

class Post(models.Model):
    titolo = models.CharField(max_length=120)
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    #python 3
    def __str__(self):
        return self.titolo

    #python 2
    def __unicode__(self):
        return self.titolo
