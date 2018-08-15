from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id','name')
