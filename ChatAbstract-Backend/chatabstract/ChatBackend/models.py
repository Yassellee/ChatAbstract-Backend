from django.db import models

# Create your models here.

class Chat(models.Model):
    text = models.TextField(max_length=10000)
    gpt = models.TextField(max_length=20000)
    #datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class Operation(models.Model):
    text = models.TextField(blank=True)
    pos_start = models.IntegerField(blank=True)
    pos_end = models.IntegerField(blank=True)
    comment = models.TextField(max_length=20000)
    #datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)