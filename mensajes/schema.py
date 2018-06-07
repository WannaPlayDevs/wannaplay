import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

import datetime

from .models import Mensaje
from usuarios.schema import UserType
from usuarios.models import User

class MensajeType(DjangoObjectType):
    class Meta:
        model = Mensaje


class Query(graphene.ObjectType):
    mensajes = graphene.List(MensajeType)
    misMensajes = graphene.List(MensajeType, fkDestinatario=graphene.String())
    

    def resolve_mensajes(self, info, **kwargs):
        return Mensaje.objects.all()

    # def resolve_misMensajes(self, info, **kwargs):
    #     # import ipdb;ipdb.set_trace()
    #     fkDestinatario = kwargs.get('fkDestinatario')
    #     if fkDestinatario is not None:
    #         return Mensaje.objects.all()
    #     return None

    def resolve_misMensajes(self, info, fkDestinatario, **kargs):
        fkDestinatario = int(fkDestinatario)
        filter = (
            Q(fkDestinatario = fkDestinatario)
        )
        return Mensaje.objects.filter(filter)


class CreateMensaje(graphene.Mutation):
    pkMensaje = graphene.Int()
    fkRemitente = graphene.Field(UserType)
    fkDestinatario = graphene.Field(UserType)
    asunto = graphene.String()
    cuerpo = graphene.String()
    fecha = graphene.types.datetime.Date()

    class Arguments:
        fkRemitente = graphene.Int()
        fkDestinatario = graphene.Int()
        asunto = graphene.String()
        cuerpo = graphene.String()

    def mutate(self, info, fkRemitente, fkDestinatario, asunto, cuerpo):
        remitente = User.objects.filter(pkUser=fkRemitente).first()
        destinatario = User.objects.filter(pkUser=fkDestinatario).first()
        fecha = datetime.date.today()

        mensaje = Mensaje(
            fkRemitente=remitente, 
            fkDestinatario=destinatario, 
            asunto=asunto, 
            cuerpo=cuerpo, 
            fecha=fecha
        )
        mensaje.save()

        return CreateMensaje(
            pkMensaje=mensaje.pkMensaje,
            fkRemitente=mensaje.fkRemitente,
            fkDestinatario=mensaje.fkDestinatario,
            asunto=mensaje.asunto,
            cuerpo=mensaje.cuerpo,
            fecha=mensaje.fecha,
        )

class UpdateMensaje(graphene.Mutation):
    # import ipdb;ipdb.set_trace()
    pkMensaje = graphene.Int()
    asunto = graphene.String()
    cuerpo = graphene.String()

    class Arguments:
        pkMensaje = graphene.Int()
        asunto = graphene.String()
        cuerpo = graphene.String()

    def mutate(self, info, pkMensaje, asunto=None, cuerpo=None):
        mensaje = Mensaje.objects.get(pkMensaje=pkMensaje)

        if(asunto is not None):
            mensaje.asunto = asunto
            mensaje.save()
        if(cuerpo is not None):
            mensaje.cuerpo = cuerpo
            mensaje.save()

        return mensaje

class DeleteMensaje(graphene.Mutation):
    pkMensaje = graphene.Int()

    class Arguments:
        pkMensaje = graphene.Int()

    def mutate(self, info, pkMensaje):
        mensaje = Mensaje.objects.get(pkMensaje=pkMensaje)
        mensaje.delete()

        return None



class Mutation(graphene.ObjectType):
    create_mensaje = CreateMensaje.Field()
    delete_mensaje = DeleteMensaje.Field()
    update_mensaje = UpdateMensaje.Field()
