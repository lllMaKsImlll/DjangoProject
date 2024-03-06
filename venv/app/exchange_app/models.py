from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    human = models.ForeignKey('Human', on_delete=models.PROTECT, null=True)

class Human(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

