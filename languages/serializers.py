#to send and recive data to rest_framework API URL
from rest_framework import serializers
from .models import Language

#class LanguageSerializer(serializers.ModelSerializer):
class LanguageSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model=Language
        fields=('id','name','paradigm','url')
