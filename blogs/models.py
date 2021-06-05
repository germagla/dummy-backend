from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.TextField(max_length=64)
    body = models.TextField(max_length=1024)
    author = models.TextField(max_length=32)

    def __str__(self):
        return self.title
