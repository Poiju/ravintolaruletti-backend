from django.db import models

class Ravintola(models.Model):
    name = models.TextField()
    photoURL = models.TextField()
    ##URLField

    class Meta:
        ordering = ['name']