from django.db import models

class Mensaje(models.Model):

    pkMensaje = models.AutoField(primary_key=True)
    fkRemitente = models.ForeignKey('usuarios.User', null=False, blank=False, on_delete=models.CASCADE, related_name='mensaje_rem')
    fkDestinatario = models.ForeignKey('usuarios.User', null=False, blank=False, on_delete=models.CASCADE, related_name='mensaje_dest')
    asunto = models.TextField(max_length=150)
    cuerpo = models.TextField(max_length=1000)
    fecha = models.DateTimeField()

