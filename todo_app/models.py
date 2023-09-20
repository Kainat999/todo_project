from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class TodoItem(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.topic


# def get_current_user():
   
#     return User.objects.get(username='admin')

class TodoItem(models.Model):
    description = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
