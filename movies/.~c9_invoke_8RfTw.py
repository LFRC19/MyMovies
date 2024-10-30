from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models):
    name = models.CharField(max_length=80)
    
    
class Person(models):
    name = models.CharField(max_length=128)


class Job(models):
    name = models.CharField(max_length=100)
    
class Genre(models):
    title = models.CharField(max_length=200)
    overv    
        