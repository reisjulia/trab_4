from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title