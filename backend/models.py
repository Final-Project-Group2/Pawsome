from django.db import models
from frontend.more_settings import TWO_VALUES_OPT
# Create your models here.

class Species(models.Model):
      OPTIONS=TWO_VALUES_OPT["SPECIES"]
      species = models.CharField(max_length=50,choices=OPTIONS)


class Sizes(models.Model):
      OPTIONS=TWO_VALUES_OPT["SIZE"]
      sizes = models.CharField(max_length=50,choices=OPTIONS)

class Breed(models.Model):
      OPTIONS=TWO_VALUES_OPT["BREED"]
      breed = models.CharField(max_length=50,choices=OPTIONS)


class Description(models.Model):
      sizes = models.TextField(max_length=250, blank=False)


class Media(models.Model):
      
      filename = models.CharField(max_length=50)
      file = models.BinaryField()


class Status(models.Model):
      OPTIONS=TWO_VALUES_OPT["STATUS"]
      sizes = models.CharField(max_length=50,choices=OPTIONS)
