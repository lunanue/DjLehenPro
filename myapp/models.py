from django.db import models

# Create your models here.

class Appak(models.Model):
    egilea = models.CharField(max_length=20)
    izena = models.CharField(max_length=50)
    deskribapen = models.TextField()

    def __str__(self):
        return u'%s' % self.izena
