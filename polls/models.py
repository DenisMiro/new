from django.db import models

class Book(models.Model):
    title = models.CharField()
    descr = models.TextField(null=True)
    author = models.CharField()
# Create your models here.
