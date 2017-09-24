from .models import JokeUser
from rest_framework import serializers


class JokeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JokeUser
        fields = ('content',)
