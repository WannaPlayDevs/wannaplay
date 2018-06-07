import graphene
from graphene_django import DjangoObjectType

from django.db.models import Max, Q

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    filterUser = graphene.List(
        UserType,
        alias=graphene.String(),
        playOverwatch = graphene.Boolean(),
        playWow = graphene.Boolean(),
        playRust = graphene.Boolean(),
        playGta = graphene.Boolean(),
        playPubg = graphene.Boolean(),
        playFortnite = graphene.Boolean()         
    )

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Invalid token!')

        return user

    def resolve_filterUser(self, info, alias="", playOverwatch=False, playWow=False, playRust=False, playGta=False, playPubg=False, playFortnite=False, **kwargs):

        if (alias == "" and (playOverwatch == False and playWow == False and playRust == False and playGta==False and playPubg==False and playFortnite==False)):
            return None
        if (alias != ""):
            filter = (
                Q(alias__icontains = alias)
            )
            return User.objects.filter(filter)
        if (alias=="" and (playOverwatch == True or playWow == True or playRust == True or playGta==True or playPubg==True or playFortnite==True)):
            #import ipdb; ipdb.set_trace()
            if(playFortnite == False):
                playFortnite=None
            if(playGta == False):
                playGta=None            
            if(playOverwatch == False):
                playOverwatch=None
            if(playPubg == False):
                playPubg=None
            if(playRust == False):
                playRust=None
            if(playWow == False):
                playWow=None
                
            filter = (
                Q(playOverwatch__exact = playOverwatch)| 
                Q(playWow__exact = playWow)| 
                Q(playRust__exact = playRust)| 
                Q(playGta__exact = playGta)| 
                Q(playPubg__exact = playPubg)| 
                Q(playFortnite__exact = playFortnite)
            )
            return User.objects.filter(filter)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        alias = graphene.String()

    def mutate(self, info, username, password, alias):
        user = User(username=username, alias=alias)
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):
    pkUser = graphene.Int()
    username = graphene.String()
    password = graphene.String()
    alias = graphene.String()
    karma = graphene.Int()
    steamName = graphene.String()
    bnetName = graphene.String()
    horarioManana = graphene.Boolean()
    horarioTarde = graphene.Boolean()
    horarioNoche = graphene.Boolean()
    horarioMadrugada = graphene.Boolean()
    playOverwatch = graphene.Boolean()
    playWow = graphene.Boolean()
    playRust = graphene.Boolean()
    playArk = graphene.Boolean()
    playGta = graphene.Boolean()
    playPubg = graphene.Boolean()
    playFortnite = graphene.Boolean()

    class Arguments:
        pkUser = graphene.Int()
        username = graphene.String()
        password = graphene.String()
        alias = graphene.String()
        karma = graphene.Int()
        steamName = graphene.String()
        bnetName = graphene.String()
        horarioManana = graphene.Boolean()
        horarioTarde = graphene.Boolean()
        horarioNoche = graphene.Boolean()
        horarioMadrugada = graphene.Boolean()
        playOverwatch = graphene.Boolean()
        playWow = graphene.Boolean()
        playRust = graphene.Boolean()
        playArk = graphene.Boolean()
        playGta = graphene.Boolean()
        playPubg = graphene.Boolean()
        playFortnite = graphene.Boolean()

    def mutate(self, info, pkUser, username=None, password=None, alias=None,
               karma=None, steamName=None, bnetName=None, horarioManana=None,
               horarioTarde=None, horarioNoche=None, horarioMadrugada=None,
               playOverwatch=None, playWow=None, playRust=None, playArk=None,
               playGta=None, playPubg=None, playFortnite=None):
        user = User.objects.get(pkUser=pkUser)

        if (username is not None):
            user.username = username
            user.save()
        if (password is not None):
            user.password = password
            user.save()
        if (alias is not None):
            user.alias = alias
            user.save()
        if (karma is not None):
            user.karma = karma
            user.save()
        if (steamName is not None):
            user.steamName = steamName
            user.save()
        if (bnetName is not None):
            user.bnetName = bnetName
            user.save()
        if (horarioManana is not None):
            user.horarioManana = horarioManana
            user.save()
        if (horarioTarde is not None):
            user.horarioTarde = horarioTarde
            user.save()
        if (horarioNoche is not None):
            user.horarioNoche = horarioNoche
            user.save()
        if (horarioMadrugada is not None):
            user.horarioMadrugada = horarioMadrugada
            user.save()
        if (playOverwatch is not None):
            user.playOverwatch = playOverwatch
            user.save()
        if (playWow is not None):
            user.playWow = playWow
            user.save()
        if (playRust is not None):
            user.playRust = playRust
            user.save()
        if (playArk is not None):
            user.playArk = playArk
            user.save()
        if (playGta is not None):
            user.playGta = playGta
            user.save()
        if (playPubg is not None):
            user.playPubg = playPubg
            user.save()
        if (playFortnite is not None):
            user.playFortnite = playFortnite
            user.save()

        return user



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
