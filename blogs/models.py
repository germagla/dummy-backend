from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.CharField(max_length=32)

    def __str__(self):
        return self.title
