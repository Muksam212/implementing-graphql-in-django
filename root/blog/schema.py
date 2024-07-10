import graphene
from graphene_django.types import DjangoObjectType
from .models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    all_mymodels = graphene.List(MyModelType)

    def resolve_all_mymodels(self, info):
        return MyModel.objects.all()