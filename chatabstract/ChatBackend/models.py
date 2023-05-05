from django.db import models

# Create your models here.

class Chat(models.Model):
    text = models.TextField(max_length=10000)
    gpt = models.TextField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Operation(models.model):
    type = models.IntegerField(blank=True)
    pos = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)