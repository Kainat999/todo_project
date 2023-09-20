from django.db import models

# Create your models here.
from django.db import models

class TodoItem(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
