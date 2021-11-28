from django.db import models

class Ravintola(models.Model):
    owner = models.ForeignKey('auth.User', related_name='ravintolat', on_delete=models.CASCADE)
    name = models.TextField()
    photoURL = models.TextField()
    ##URLField

    def save(self, *args, **kwargs):
   
        super(Ravintola, self).save(*args, **kwargs)

        class Meta:
            ordering = ['name']