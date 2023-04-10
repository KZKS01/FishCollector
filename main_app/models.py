from django.db import models

# Create your models here.
# define a class that inherits from models.Model
class Fish(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name