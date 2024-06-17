from django.db import models

# Create your models here.

class Clup(models.Model):
    name = models.CharField(max_length=200)
    money = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name,self.money)
