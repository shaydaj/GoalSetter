from django.db import models
from django.contrib.auth.models import User
from requests import delete

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    goals = models.TextField(null=True, blank=True)
    obstacles = models.TextField(null=True, blank=True)
     
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']