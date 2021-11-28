from django.db.models import fields
from rest_framework import serializers
from ravintolat.models import Ravintola
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    ravintolat = serializers.PrimaryKeyRelatedField(many=True, queryset=Ravintola.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'ravintolat']

class RavintolaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Ravintola
        fields = ['name', 'photoURL','owner']

