from django.db import models

class Amigo(models.Model):

    pkAmigo = models.AutoField(primary_key=True)
    fkUser1 = models.IntegerField(null=False, blank=False)
    fkUser2 = models.IntegerField(null=False, blank=False)
    estado = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField()

