from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

def myoverridenmeta(name, bases, adict):
    newClass = type(name, bases, adict)
    for field in newClass._meta.fields:
        if field.attname == 'last_login':
            field.column = 'last_login_date'
            field.db_column = 'last_login_date'
    return newClass

class User(AbstractBaseUser):

    pkUser = models.AutoField(primary_key=True)
    username = models.TextField(null=False, blank=False, max_length=25, unique=True)
    password = models.TextField(null=False, blank=False, max_length=25)
    alias = models.TextField(null=False, blank=False, max_length=25)
    karma = models.IntegerField(default=0, null=True)
    steamName = models.TextField(null=True)
    bnetName = models.TextField(null=True)
    horarioManana = models.BooleanField(default=False)
    horarioTarde = models.BooleanField(default=False)
    horarioNoche = models.BooleanField(default=False)
    horarioMadrugada = models.BooleanField(default=False)
    playOverwatch = models.BooleanField(default=False)
    playWow = models.BooleanField(default=False)
    playRust = models.BooleanField(default=False)
    playArk = models.BooleanField(default=False)
    playGta = models.BooleanField(default=False)
    playPubg = models.BooleanField(default=False)
    playFortnite = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['alias']
    
    __metaclass__ = myoverridenmeta