from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1337)


class Company(models.Model):
    name = models.TextField()
    owner = models.TextField()
    date_foundation = models.DateField()
