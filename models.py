from django.db import models

class Backend_Developer(models.Model):
    name = models.CharField(max_length=20)
    contribution = models.IntegerField()
    years_old = models.IntegerField()
    special_needs = models.BooleanField()

    def __str__(self):
        return self.name 

class Frontend_Developer(models.Model):
    name = models.CharField(max_length=20)
    contribution = models.IntegerField()
    years_old = models.IntegerField()
    special_needs = models.BooleanField()

    def __str__(self):
        return self.name 
