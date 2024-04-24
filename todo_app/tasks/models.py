from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    deadline = models.DateField()
    
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    document = models.CharField(max_length=30)