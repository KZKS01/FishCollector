from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# define a class that inherits from models.Model
class Fish(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # reverse will try to look up a url based on the name
        # send users to the detail page when new fish is created
        return reverse('fish_detail', kwargs={'fish_id': self.id})