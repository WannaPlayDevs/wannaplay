import graphene
from graphene_django import DjangoObjectType

from .models import Amigo


class AmigoType(DjangoObjectType):
    class Meta:
        model = Amigo


class Query(graphene.ObjectType):
    amigos = graphene.List(AmigoType)

    def resolve_amigos(self, info, **kwargs):
        return Amigo.objects.all()


class CreateAmigo(graphene.Mutation):
    pkAmigo = graphene.Int()
    fkUser1 = graphene.Int()
    fkUser2 = graphene.Int()
    estado = graphene.Int()
    fecha = graphene.String()

    class Arguments:
        fkUser1 = graphene.Int()
        fkUser2 = graphene.Int()
        estado = graphene.Int()
        fecha = graphene.String()

    def mutate(self, info, fkUser1, fkUser2, estado, fecha):
        amigo = Amigo(fkUser1o=fkUser1, fkUser2=fkUser2, estado=estado, fecha=fecha)
        amigo.save()

        return CreateAmigo(
            pk_amigos=amigo.pkAmigo,
            fk_userUno=amigo.fkUser1,
            fk_userDos=amigo.fkUser2,
            estado=amigo.estado,
            fecha=amigo.fecha,
        )


class DeleteAmigo(graphene.Mutation):
    pkAmigo = graphene.Int()

    class Arguments:
        pkAmigo = graphene.Int()

    def mutate(self, info, pkAmigo):
        amigo = Amigo.objects.get(pkAmigo=pkAmigo)
        amigo.delete()

        return None


class Mutation(graphene.ObjectType):
    create_amigo = CreateAmigo.Field()
    delete_amigo = DeleteAmigo.Field()
