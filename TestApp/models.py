from django.db import models

# Create your models here.
class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length = 64)


class teacher(models.Model):
    name = models.CharField(max_length = 64)
    designation = models.CharField(max_length = 64)

class book(models.Model):
    name = models.CharField(max_length = 64)
    author = models.CharField(max_length = 64)
