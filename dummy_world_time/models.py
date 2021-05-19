from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=32)
    current_time = models.TimeField(auto_now=True)
    time_offset = models.IntegerField(default=0)

    def __str__(self):
        return self.name
